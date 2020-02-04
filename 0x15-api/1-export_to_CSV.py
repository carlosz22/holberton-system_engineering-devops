#!/usr/bin/python3
"""Gather data from an API and export the data to a CSV file"""

import csv
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
        csv_list = []
        task_data = []
        for task in todo_data:
            task_data = [employee_id,
                         employee_username,
                         str(task.get('completed')),
                         task.get('title')]
            csv_list.append(task_data)

        with open(employee_id + '.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            for row in csv_list:
                writer.writerow(row)
