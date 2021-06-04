### IMPORT MODULES ###
import tweepy
import random
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from dotenv import load_dotenv

### IMPORT TASKS ###
from currencies.main import get_prices, prices
from history.main import get_history_events, title, facts
from youtube.main import get_youtube_video, title, link

load_dotenv()

### TWITTER API ###
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



### ACTUAL TWEETS ###
# Currencies
def tweet_currencies(prices):
    api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# History
def tweet_history_events(title, facts):
    fact = random.choice(facts)
    api.update_status(status = f"{title}\n\n{fact}\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nzdroj: https://wikipedia.cz\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# Latest YouTube video
def tweet_youtube_video(title, link):
    if title == None or link == None:
        sys.exit()
    else:
        api.update_status(status = f"Nové video na YouTube! 😍\n\n{title}\n{link}\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
        sys.exit()



### SCHEDULER ###
sched = BlockingScheduler()

# Currencies tweets
@sched.scheduled_job('cron', hour='0,12')
def timed_currencies():
    tweet_currencies(prices)

# History tweets
@sched.scheduled_job('cron', hour='20')
def timed_history_events():
    tweet_history_events(title, facts)

# YouTube tweets
@sched.scheduled_job('cron', hour='15')
def timed_youtube_video():
    tweet_youtube_video(title, link)

sched.start()
