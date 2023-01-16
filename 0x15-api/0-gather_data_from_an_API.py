#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    result = requests.get(user)
    json_o = result.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todo = '{}todo?userId={}'.format(url, sys.argv[1])
    result = requests.get(todo)
    tasks = result.json()
    list_tasks = []
    for task in tasks:
        if task.get('Completed') is True:
            list_tasks.append(task)

    print("({}/{}):".format(len(list_tasks), len(tasks)))
    for task in list_tasks:
        print("\t {}".format(tasks.get("title")))
