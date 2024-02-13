#!/usr/bin/python3
"""
Script to make request to the reddit API
and compute the total subscribers of
a specifit subreddit
"""


def number_of_subscribers(subreddit):
    import requests
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Agent-Lamin"},
        allow_redirects=False,
    )
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
