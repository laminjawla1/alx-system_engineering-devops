#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, sys.argv[1])).json()
    todos = requests.get(
            "{}/todos".format(url), params={"userId": sys.argv[1]}).json()

    todos_completed = get_total_todos_completed(todos)
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), todos_completed, len(todos)
        )
    )
    for todo in todos:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))


def get_total_todos_completed(todos):
    total = 0
    for todo in todos:
        if todo.get("completed"):
            total += 1
    return total


if __name__ == "__main__":
    main()
