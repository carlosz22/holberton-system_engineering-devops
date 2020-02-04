#!/usr/bin/python3
"""Gather data from an API and export the data to a JSON file"""

import json
import requests

if __name__ == '__main__':
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_employee = 'https://jsonplaceholder.typicode.com/users'
    todo_data = requests.get(url_todo)
    employee_data = requests.get(url_employee)
    try:
        todo_data = todo_data.json()
        employee_data = employee_data.json()
    except:
        todo_data = []
        employee_data = []

    employees_tasks = {}
    for employee in employee_data:
        employee_id = employee.get('id')
        employee_username = employee.get('username')
        tasks_list = []
        for task in todo_data:
            if task.get('userId') == employee_id:
                task_dict = {'task': task.get('title'),
                             'completed': task.get('completed'),
                             'username': employee_username}
                tasks_list.append(task_dict)
        employees_tasks.update({employee_id: tasks_list})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(employees_tasks, file)
