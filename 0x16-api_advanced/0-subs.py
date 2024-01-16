#!/usr/bin/python3
""" 
reddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the subreddit exists
        if 'error' in data:
            return 0

        return data['data']['subscribers']
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"{subscribers}")
