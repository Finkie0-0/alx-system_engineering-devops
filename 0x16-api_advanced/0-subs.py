#!/usr/bin/python3
"""
script of a function that queries the Reddit API and returns the number of subscribers
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    user_agent = 'Mozilla/5.0'

    headers = {
        "User-Agent": user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    d = res.json()
    if "data" not in d:
        return 0
    if "subscribers" not in d.get('data'):
        return 0
    return res.json()['data']['subscribers']
