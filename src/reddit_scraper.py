import praw
import sqlite3
import logging

from src.database import insert_reddit_post
from config.config import load_config

# Configure logging
logger = logging.getLogger(__name__)

# Load configuration settings
config = load_config()
REDDIT_CLIENT_ID = config['reddit_client_id']
REDDIT_CLIENT_SECRET = config['reddit_client_secret']
REDDIT_USER_AGENT = config['reddit_user_agent']
REDDIT_POST_LIMIT = config['reddit_post_limit']

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def scrape_reddit(subreddits):
    try:        
        post_count = 0
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            logger.info(f'Scraping new posts from subreddit: {subreddit_name}')
            for post in subreddit.new(limit=REDDIT_POST_LIMIT):
                post_id = post.id
                content = post.selftext
                timestamp = post.created_utc  # Unix timestamp
                author = post.author.name if post.author else 'Deleted'

                insert_reddit_post(post_id, content, timestamp, author)
        
        logger.info(f'{post_count} new Reddit posts scraped and saved.')
    
    except Exception as e:
        logger.error(f'An error occurred while scraping Reddit: {e}')