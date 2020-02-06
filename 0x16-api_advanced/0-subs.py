#!/usr/bin/python3
"""Get number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers for a subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    user_agent_header = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/80.0.3987.87 Safari/537.36'
    r = requests.get(url, allow_redirects=False,
                     headers={'User-Agent': user_agent_header})
    subscribers = 0
    if r.status_code == 200:
        try:
            data = r.json()
            subscribers = data.get('data', 0).get('subscribers', 0)
        except:
            pass
    return subscribers
