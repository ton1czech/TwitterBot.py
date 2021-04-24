# Import Modules
import tweepy
import random
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from dotenv import load_dotenv

from currencies.main import get_prices, prices
from history.main import get_history_events, title, facts

load_dotenv()

# Set up Twitter API
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# The actual currencies tweet
def tweet_currencies(prices):
    api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nsource code: https://github.com/ton1czech/gingy")

# The actual history tweet
def tweet_history_events(title, facts):
    fact = random.choice(facts)
    api.update_status(status = f"{title}\n\n{fact}\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nzdroj: https://wikipedia.cz\nsource code: https://github.com/ton1czech/gingy")

# Schedule the processes
sched = BlockingScheduler()

# Schedule currencies tweets
@sched.scheduled_job('cron', hour='0,12')
def timed_currencies():
    tweet_currencies(prices)

# Schedule history tweets
@sched.scheduled_job('cron', hour='5')
def timed_history_events():
    tweet_history_events(title, facts)

sched.start()
