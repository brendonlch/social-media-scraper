import tweepy
import sqlite3
import logging

from src.database import insert_tweet
from config.config import load_config

# Configure logging
logger = logging.getLogger(__name__)

# Load configuration settings
config = load_config()
X_API_KEY = config['x_api_key']
X_API_SECRET_KEY = config['x_api_secret_key']
X_ACCESS_TOKEN = config['x_access_token']
X_ACCESS_TOKEN_SECRET = config['x_access_token_secret']

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET_KEY)
auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def scrape_twitter(keywords):
    try:        
        logger.info(f'Scraping new posts with keywords: {keywords}')
        # Search for tweets using the specified keywords
        tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang='en', tweet_mode='extended').items(100)
        
        tweet_count = 0
        for tweet in tweets:
            tweet_id = tweet.id_str
            content = tweet.full_text
            timestamp = tweet.created_at
            author = tweet.author.screen_name

            insert_tweet(tweet_id, content, timestamp, author)
        
        logger.info(f'{tweet_count} new tweets scraped and saved.')
        
    except Exception as e:
        logger.error(f'An error occurred: {e}')