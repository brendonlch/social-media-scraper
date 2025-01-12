import time
import logging

from src.twitter_scraper import scrape_twitter
from src.reddit_scraper import scrape_reddit
from src.database import initialize_database
from src.logging import setup_logging
from config.config import load_config

def main():
    # Configure logging
    setup_logging()
    logger = logging.getLogger(__name__)
    # Initialize the database
    initialize_database()
    # Load configuration settings
    config = load_config()
    
    # Retrieve settings from the configuration
    SCRAPING_INTERVAL = config['scraping_interval']
    KEYWORDS = config['keywords']
    SUBREDDITS = config['subreddits']
    
    while True:
        try:
            logger.info("Starting scraping process.")

            # Scrape Twitter
            scrape_twitter(KEYWORDS)
            # Scrape Reddit
            scrape_reddit(SUBREDDITS)

            logger.info("Scraping completed. Sleeping for %s seconds.", SCRAPING_INTERVAL)
            time.sleep(SCRAPING_INTERVAL)
        except Exception as e:
            logger.error("An error occurred during scraping: %s", e)

if __name__ == "__main__":
    main()