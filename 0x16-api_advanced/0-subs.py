#!/usr/bin/python3
"""
A script to get the total subscribers
of a specified subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(sys.argv[1]),
        headers={"User-Agent": "I-Am-Agent-Sage"},
        allow_redirects=False,
    )
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers", 0)
