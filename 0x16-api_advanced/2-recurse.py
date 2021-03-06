#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function
should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ print the title of the hottest topics """
    if not after:
        url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
            .format(subreddit, after)
    head = {"User-Agent": "Mozilla/5.0"}
    j_response = requests.get(url, headers=head).json()

    if 'error' in j_response:
        return(None)
    else:
        data = j_response.get('data').get('children')
        for obj in data:
            hot_list.append(obj.get('data').get('title'))
        after = j_response.get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
