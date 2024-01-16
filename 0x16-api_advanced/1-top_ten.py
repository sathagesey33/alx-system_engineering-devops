#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10
    hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Construct the URL for the hot posts API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the subreddit exists
        if 'error' in data:
            print(None)
            return

        # Extract and print titles of the first 10 hot posts
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    except Exception as e:
        # Handle exceptions (e.g., network issues, JSON parsing errors)
        print(f"Error: {e}")
        print(None)


# Example usage
if __name__ == '__main__':
    import sys

    # Check if a subreddit name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
