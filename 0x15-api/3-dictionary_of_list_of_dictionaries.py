#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()

    tasks = init(users)

    for user in users:
        user_id = user.get("id")
        todos = requests.get(
                "{}/todos".format(url), params={"userId": user_id}).json()
        username = user.get("username")

        for todo in todos:
            tasks[user_id].append(
                {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
            )
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks, jsonfile)


def get_total_todos_completed(todos):
    total = 0
    for todo in todos:
        if todo.get("completed"):
            total += 1
    return total


def init(users):
    return {user.get("id"): [] for user in users}


if __name__ == "__main__":
    main()
