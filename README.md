# Social Media Data Scraper
A Python-based scraper that continuously collects tweets and Reddit posts based on specified keywords and subreddits, storing the data in a local SQLite database.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Scraper](#running-the-scraper)
6. [Project Structure](#project-structure)
7. [Usage Examples](#usage-examples)
8. [Logging](#logging)

---

## Project Overview

This project collects social media data from Twitter and Reddit, storing it in a local SQLite database for further analysis. The scraper runs continuously, fetching new posts at regular intervals.

## Prerequisites

* Python 3.8 or higher
* Internet connection to access Twitter and Reddit APIs
* SQLite database (provided locally)

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/brendonlch/social-media-scraper.git
   cd social-media-scraper
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set up API credentials:**

   * Obtain Twitter API keys from [Twitter Developer Portal](https://developer.twitter.com/).
   * Obtain Reddit API credentials from [Reddit Developer Portal](https://www.reddit.com/prefs/apps).
   * Update `config/config.py` with your API keys and other configuration settings.


## Configuration

* **API Credentials:** Store your Twitter and Reddit API keys in `config/config.py`.
* **Scraping Settings:** Adjust keywords, subreddits, and scraping intervals in `config/config.py`.
* **Database Path:** Ensure the database path in `config/config.py` is correct.



## Running the Scraper

1. **Start the scraper:**
   ```
   python main.py
   ```
2. **The scraper will:**
   * Connect to Twitter and Reddit APIs.
   * Fetch new posts based on the specified keywords and subreddits.
   * Store the data in the SQLite database.
   * Log activities to `logs/scraper.log`.
   * Run in an infinite loop, scraping data every interval specified in `config/config.py`.


## Project Structure

```
SocialMediaScraper/
├── data/
│   └── social_media_data.db
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── twitter_scraper.py
│   ├── reddit_scraper.py
│   └── database.py
├── logs/
│   └── scraper.log
├── config/
│   └── config.py
├── README.md
├── main.py
└── requirements.txt
```


## Usage Examples

* **Reading Data from the Database:**
  ```
  import sqlite3

  # Connect to the database
  conn = sqlite3.connect('data/social_media_data.db')
  cursor = conn.cursor()

  # Example query: Fetch all tweets
  cursor.execute("SELECT * FROM tweets")
  tweets = cursor.fetchall()
  for tweet in tweets:
      print(tweet)

  # Close the connection
  conn.close()
  ```
* **Adding New Keywords or Subreddits:**

  * Modify the `KEYWORDS` and `SUBREDDITS` lists in `config/config.py`.



## Logging

* **Log File:** `logs/scraper.log`
* **Log Format:** `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
* **Log Levels:** INFO, WARNING, ERROR, CRITICAL

The log file records all scraper activities, including data collection, database operations, and errors.
