#!/usr/bin/python3

""" Function to count words in all hot posts of a given Reddit subreddit. """

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Function to count words in all hot posts of a given Reddit subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {'User-Agent': 'Python/requests'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        for word in word_list:
            word = word.lower()
            if word not in word_dict.keys():
                word_dict[word] = 0
        hot_posts = r.json().get('data').get('children')
        for post in hot_posts:
            title = post.get('data').get('title').lower().split()
            for word in word_dict.keys():
                word_dict[word] += title.count(word)
        after = r.json().get('data').get('after')
        if after is None:
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                if value > 0:
                    print('{}: {}'.format(key, value))
        else:
            return count_words(subreddit, word_list, after, word_dict)
    else:
        return None
