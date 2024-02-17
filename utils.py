import requests
import random

def fetch_reddit_data(subreddit, limit=100):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all&limit={limit}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_random_post(data):
    posts = data['data']['children']
    return random.choice(posts)['data']