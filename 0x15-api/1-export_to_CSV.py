#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [user_id, username, todo.get("completed"), todo.get("title")]
            )


def get_total_todos_completed(todos):
    total = 0
    for todo in todos:
        if todo.get("completed"):
            total += 1
    return total


if __name__ == "__main__":
    main()
