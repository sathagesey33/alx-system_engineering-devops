#!/usr/bin/python3
""" recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The identifier for the starting point of the next page.

    Returns:
        list: A list containing the titles of
        all hot articles for the subreddit.
              Returns None if the subreddit is not valid or 
              no results are found.
    """
    # Base case: If the subreddit is not valid, return None
    if subreddit is None:
        return None

    # Construct the URL for the hot posts API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header

    try:
        # Add 'after' parameter for pagination
        params = {'after': after} if after else {}

        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Check if the subreddit exists
        if 'error' in data:
            return None

        # Extract titles and add them to the hot_list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        # Recursively call the function with the next page's 'after' value
        if data['data']['after']:
            return recurse(subreddit, hot_list, after=data['data']['after'])
        else:
            return hot_list

    except Exception as e:
        # Handle exceptions (e.g., network issues, JSON parsing errors)
        print(f"Error: {e}")

return None


# Example usage
if __name__ == '__main__':
    import sys

    # Check if a subreddit name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
