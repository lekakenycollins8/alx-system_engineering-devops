#!/usr/bin/python3
"""queries Reddit API"""


import requests


def top_ten(subreddit):
    """prints titles of the first ten hot posts of a subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = {"User-Agent": "your bot 0.1"}
    parameters = {"limit": 10}

    response = requests.get(url, headers=user_agent, params=parameters)
    try:
        data = response.json()
        hot_posts = data.get('data').get('children')

        for i in hot_posts:
            print(i.get('data').get('title'))
    except Exception:
        print("None")
