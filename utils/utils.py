import requests
import random

def fetch_reddit_data(subreddits, limit=1000):
    subreddit = random.choice(subreddits)  # Select a random subreddit from the list
    url = f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all&limit={limit}"
    # Use a more descriptive User-Agent string
    headers = {'User-Agent': 'RahRedditApp/1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        # Check if the response status code is 200 (OK)
        response.raise_for_status()
        # Ensure the response is in JSON format
        if 'application/json' in response.headers.get('Content-Type'):
            data = response.json()
            return data
        else:
            # Handle unexpected content type
            print(f"Unexpected content type: {response.headers.get('Content-Type')}")
    except requests.exceptions.RequestException as e:
        # Handle request errors (including status code errors)
        print(f"Request failed: {e}")
    
    # Return None or a default value if the request fails
    return None

def get_random_text_post(data):
    posts = data['data']['children']
    return random.choice(posts)['data']

def get_random_image_post(data, attempts=0):
    posts = data['data']['children']
    post = random.choice(posts)['data']
    
    if 'post_hint' in post and post['post_hint'] == 'image':
        return post

    elif attempts > 10:
        return None  # Or return a default image post

    else:
        return get_random_image_post(data, attempts + 1)