# Configuration settings for the social media data scraper

# Twitter API credentials
x_api_key = 'YOUR_TWITTER_API_KEY'
x_api_secret_key = 'YOUR_TWITTER_API_SECRET_KEY'
x_access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
x_access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Reddit API credentials
reddit_client_id = 'YOUR_REDDIT_CLIENT_ID'
reddit_client_secret = 'YOUR_REDDIT_CLIENT_SECRET'
reddit_user_agent = 'YOUR_USER_AGENT'
reddit_post_limit = 1000 # number of reddit posts to fetch per interval

# Database configuration
db_path = 'data/social_media_data.db'

# Scraping settings
scraping_interval = 3600  # in seconds (1 hour)
keywords = ['python', 'data science', 'machine learning']
subreddits = ['python', 'datascience', 'machinelearning']

# Configuration dictionary
config = {
    'x_api_key': x_api_key,
    'x_api_secret_key': x_api_secret_key,
    'x_access_token': x_access_token,
    'x_access_token_secret': x_access_token_secret,
    'reddit_client_id': reddit_client_id,
    'reddit_client_secret': reddit_client_secret,
    'reddit_user_agent': reddit_user_agent,
    'db_path': db_path,
    'scraping_interval': scraping_interval,
    'keywords': keywords,
    'subreddits': subreddits,
    'reddit_post_limit': reddit_post_limit
}

# Function to load configuration settings
def load_config():
    return config