#!/usr/bin/python3
"""Uses REST API to gather dater for a given employee"""


import requests
from sys import argv

if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeId = argv[1]
    url = baseUrl + '/' + employeeId
    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeId, username, task.get('completed'), task.get('title')))
