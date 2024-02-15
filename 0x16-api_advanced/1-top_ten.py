#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "Agent-Lamin"},
        allow_redirects=False,
    )
    if response.status_code >= 300:
        print(None)
    else:
        for r in response.json().get("data").get("children"):
            print(r.get("data").get("title"))
