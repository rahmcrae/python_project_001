import requests
import random

def fetch_reddit_data(subreddits, limit=100):
    subreddit = random.choice(subreddits)  # Select a random subreddit from the list
    url = f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all&limit={limit}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_random_text_post(data):
    posts = data['data']['children']
    return random.choice(posts)['data']

def get_random_image_post(data, attempts=0):
    posts = data['data']['children']
    post = random.choice(posts)['data']
    # Limit the number of attempts to prevent infinite recursion
    if attempts > 10:
        return None  # Or return a default image post
    if 'post_hint' in post and post['post_hint'] == 'image':
        return post
    else:
        return get_random_image_post(data, attempts + 1)