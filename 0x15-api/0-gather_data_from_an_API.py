#!/usr/bin/python3
"""Uses REST API to gather dater for a given employee"""


import requests
from sys import argv

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeId = argv[1]
    url = baseUrl + '/' + employeeId
    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks ({}/{}):".format(
        employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
