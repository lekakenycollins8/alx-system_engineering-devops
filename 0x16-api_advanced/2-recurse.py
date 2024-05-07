#!/usr/bin/python3
"""queries the Reddit API"""


import requests

def recurse(subreddit, hot_list=[], after=None):
    """returns a list of titles for hot articles"""
    if not subreddit or not isinstance(subreddit, str):
        return None
    user_agent = {"User-Agent": "your bot 0.1"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=user_agent, params=params)
        data = response.json()
        children = data.get('data', {}).get('children', [])

        for child in children:
            title = child.get('data', {}).get('title')
            if title:
                hot_list.append(title)
        
        after = data.get('data', {}).get('after')
        if after:
            recurse(subreddit, hot_list, after)

        return hot_list

    except Exception:
        return None
