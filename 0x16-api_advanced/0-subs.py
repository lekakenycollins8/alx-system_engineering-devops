#!/usr/bin/python3
"""Gets number of subscribers of a subreddit"""


import requests
from sys import argv

def number_of_subscribers(subreddit):
    """returns total no.of subscribers of a subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers={"User-Agent": "Google Chrome Version 81.0.4044.129"})
    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                subscriber_count = data['data']['subscribers']
                return subscriber_count
        except (KeyError, ValueError):
            pass
    return 0
