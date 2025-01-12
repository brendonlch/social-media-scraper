import sqlite3
import logging 

from config.config import load_config

# Load configuration settings
config = load_config()
DB_PATH = config['db_path']

# Configure logging
logger = logging.getLogger(__name__)

def initialize_database():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # Create tweets table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tweets (
                    id TEXT PRIMARY KEY,
                    content TEXT,
                    timestamp INTEGER,
                    author TEXT
                )
            ''')
            # Create reddit_posts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reddit_posts (
                    id TEXT PRIMARY KEY,
                    content TEXT,
                    timestamp INTEGER,
                    author TEXT
                )
            ''')
            conn.commit()
            logger.info("Database initialized.")
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")

def insert_tweet(tweet_id, content, timestamp, author):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tweets WHERE id = ?', (tweet_id,))
            if not cursor.fetchone():
                cursor.execute('''
                    INSERT INTO tweets (id, content, timestamp, author)
                    VALUES (?, ?, ?, ?)
                ''', (tweet_id, content, timestamp, author))
                conn.commit()
                logger.info(f"Tweet {tweet_id} inserted into database.")
            else:
                logger.info(f"Tweet {tweet_id} already exists.")
    except sqlite3.Error as e:
        logger.error(f"Error inserting tweet {tweet_id}: {e}")

def insert_reddit_post(post_id, content, timestamp, author):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reddit_posts WHERE id = ?', (post_id,))
            if not cursor.fetchone():
                cursor.execute('''
                    INSERT INTO reddit_posts (id, content, timestamp, author)
                    VALUES (?, ?, ?, ?)
                ''', (post_id, content, timestamp, author))
                conn.commit()
                logger.info(f"Reddit post {post_id} inserted into database.")
            else:
                logger.info(f"Reddit post {post_id} already exists.")
    except sqlite3.Error as e:
        logger.error(f"Error inserting Reddit post {post_id}: {e}")