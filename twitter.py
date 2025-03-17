import os
import tweepy
import time
import random
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API Credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Initialize Twitter Client
twitter_client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Track last replied tweet
last_replied_tweet = None

# GM/GN reply messages
gm_replies = ["Gm {username}!", "gm mate!", "Good morning!", "gm gm!", "Grand rising ☀️"]
gn_replies = ["Gn {username}!", "Good night!", "Sleep well!", "Sweet dreams 🌙"]

# Function to fetch the latest GM/GN tweet
def get_latest_tweet():
    global last_replied_tweet

    query = "(GM OR Gm OR gm OR Good morning OR GN OR Gn OR gn OR Good night) -is:retweet -is:reply"

    try:
        tweets = twitter_client.search_recent_tweets(query=query, max_results=10, tweet_fields=["author_id"], expansions=["author_id"])

        if tweets.data:
            user_data = {user.id: user.username for user in tweets.includes.get('users', [])}

            for latest_tweet in tweets.data:
                tweet_id = latest_tweet.id
                tweet_text = latest_tweet.text
                author_id = latest_tweet.author_id

                if last_replied_tweet == tweet_id:
                    continue  # Skip if already replied

                username = user_data.get(author_id, "friend")  
                last_replied_tweet = tweet_id
                return tweet_id, tweet_text, username  

    except tweepy.errors.TooManyRequests as e:
        reset_time = int(e.response.headers["x-rate-limit-reset"])
        wait_time = reset_time - int(datetime.datetime.utcnow().timestamp())

        # 🔹 Cap the max wait time to 900 seconds (15 minutes)
        if wait_time > 900:
            wait_time = 900

        print(f"\033[91m❌ Rate limit exceeded! Waiting {wait_time} seconds...\033[0m")
        
        # 🔹 Dynamic wait: check every 2 minutes instead of waiting the full time at once
        while wait_time > 0:
            print(f"\033[93m⏳ Waiting {wait_time} seconds...\033[0m", end="\r")
            time.sleep(120)  # Sleep for 2 minutes
            wait_time -= 120  # Reduce the remaining time

        return None, None, None

    except Exception as e:
        print(f"\033[91m❌ Unexpected error: {e}\033[0m")
        return None, None, None

    return None, None, None

# Function to auto-reply
def auto_reply():
    tweet_id, tweet_text, username = get_latest_tweet()

    if tweet_id:
        # Select a reply message
        if "GM" in tweet_text.upper():
            reply_text = random.choice(gm_replies).format(username=username)
        elif "GN" in tweet_text.upper():
            reply_text = random.choice(gn_replies).format(username=username)
        else:
            return

        # Send reply
        twitter_client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        print(f"\033[92m✅ Replied: {reply_text}\033[0m")  # Green text in terminal

# Function to continuously check for new tweets
def start_reply_bot():
    print("\033[92m🚀 GMGN AutoReply Bot is running...\033[0m")
    while True:
        auto_reply()
        time.sleep(180)  # Check every 3 minutes (180 seconds)

# Start the bot
if __name__ == "__main__":
    start_reply_bot()