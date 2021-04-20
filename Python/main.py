# Import Modules
import tweepy
import pandas_datareader.data as data
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from currencies import get_prices
from dotenv import load_dotenv

load_dotenv()

# Set up Twitter API
with open('../keys.txt') as f:
    content = f.read().splitlines()

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Getting different data
get_prices(data)            # get currencies and their prices

# The actual tweet
def write_tweet(prices):
    api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nsource code: https://github.com/ton1czech/gingy")

# Schedule the process
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='0,12')
def timed_job():
    write_tweet(prices)

sched.start()