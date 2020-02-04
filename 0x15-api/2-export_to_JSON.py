#!/usr/bin/python3
"""Gather data from an API and export the data to a JSON file"""

import json
import requests
import sys

if __name__ == '__main__':
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_employee = 'https://jsonplaceholder.typicode.com/users'
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        todo_data = requests.get(url_todo, params={'userId': employee_id})
        employee_data = requests.get(url_employee, params={'id': employee_id})
        try:
            todo_data = todo_data.json()
            employee_data = employee_data.json()
        except:
            todo_data = []
            employee_data = []

        employee_username = employee_data[0].get('username')
        tasks_list = []
        task_dict = {}
        for task in todo_data:
            task_dict = {'task': task.get('title'),
                         'completed': task.get('completed'),
                         'username': employee_username}
            tasks_list.append(task_dict)
        export_json = {employee_id: tasks_list}

        with open(employee_id + '.json', 'w') as file:
            json.dump(export_json, file)
