#!/usr/bin/python3
"""
A script to get the total subscribers of a subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(sys.argv[1]),
        headers={"User-Agent": "I-Am-Agent-Sage"},
    )
    data = response.json().get("data")
    return data.get("subscribers", 0) if data else 0
