from flask import *
from utils.utils import *
from utils.subreddit_list import *

app = Flask(__name__)

@app.route('/')
def home():     
    # Fetch data from a random subreddit from the provided lists
    image_data = fetch_reddit_data(image_subreddits)
    text_data = fetch_reddit_data(text_subreddits)
    
    image_post = get_random_image_post(image_data)
    quote_post = get_random_text_post(text_data)
    
    return render_template('index.html', image_post=image_post, quote_post=quote_post)

if __name__ == '__main__':
    app.run( debug=True)