#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
"""


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python3'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
