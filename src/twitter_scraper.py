import tweepy
import sqlite3
import logging

from src.database import insert_tweet
from config.config import load_config

# Configure logging
logger = logging.getLogger(__name__)

# Load configuration settings
config = load_config()
TWITTER_API_KEY = config['twitter_api_key']
TWITTER_API_SECRET_KEY = config['twitter_api_secret_key']
TWITTER_ACCESS_TOKEN = config['twitter_access_token']
TWITTER_ACCESS_TOKEN_SECRET = config['twitter_access_token_secret']

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
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