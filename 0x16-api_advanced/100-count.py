#!/usr/bin/python3
"""queries reddit API"""


import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    """prints a sorted count of given words"""
    if not subreddit or not isinstance(subreddit, str):
        return

    user_agent = {"User-Agent": "your bot 0.1"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {'after': after} if after else {}

    response = requests.get(url, headers=user_agent, params=params)
    data = response.json()
    children = data.get('data', {}).get('children', [])
    titles = [child.get('data', {}).get('title', '') for child in children]
    for title in titles:
        for word in word_list:
            if word.lower() in title.lower():
                word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1
    after = data.get('data', {}).get('after')
    if after:
        count_words(subreddit, word_list, after, word_counts)
    if after is None:
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
