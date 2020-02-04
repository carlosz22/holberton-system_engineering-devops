#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

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

    employee_name = employee_data[0].get('name')
    total_tasks = len(todo_data)
    tasks_completed = 0
    tasks_completed_description = []
    for task in todo_data:
        if task.get('completed'):
            tasks_completed += 1
            tasks_completed_description.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, tasks_completed, total_tasks))
    for task in tasks_completed_description:
        print('\t {}'.format(task))
