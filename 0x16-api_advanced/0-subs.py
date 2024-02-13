#!/usr/bin/python3
"""
A script to get the total subscribers
of a specified subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
