#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    list_task = []
    for task in tasks:
        if task.get('completed') is True:
            list_task.append(task)

    print("({}/{}):".format(len(list_task), len(tasks)))
    for task in list_task:
        print("\t {}".format(task.get("title")))
