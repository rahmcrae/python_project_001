from flask import *
from utils import *

app = Flask(__name__)

@app.route('/')
def home():
    image_data = fetch_reddit_data('earthporn')
    text_data = fetch_reddit_data('science')
    
    image_post = get_random_post(image_data)
    quote_post = get_random_post(text_data)
    
    # return image_post,quote_post
    return render_template('index.html', image_post=image_post, quote_post=quote_post)

if __name__ == '__main__':
    app.run(debug=True)
