#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        for post in res.json().get("data").get("children"):
            print(post.get("data").get("title"))
        return
    print(None)
