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
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    username = user.get("username")
    todos = requests.get(
            "{}/todos".format(url), params={"userId": user_id}).json()

    todos_completed = get_total_todos_completed(todos)
    tasks = {user_id: []}
    for todo in todos:
        tasks[user_id].append(
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username,
            }
        )
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(tasks, jsonfile)


def get_total_todos_completed(todos):
    total = 0
    for todo in todos:
        if todo.get("completed"):
            total += 1
    return total


if __name__ == "__main__":
    main()
