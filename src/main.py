### IMPORT MODULES ###
import tweepy
import random
import time
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from dotenv import load_dotenv

load_dotenv()



### IMPORT TASKS ###
from currencies.main import fetch_currencies
from history.main import fetch_history
from youtube.main import fetch_youtube
from weather.main import fetch_weather



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
    if prices == None:
        pass
    else:
        api.update_status(status = f"Bitcoin: ${prices[0]}    #bitcoin\nEthereum: ${prices[1]}    #ethereum\nDogecoin: ${prices[2]}    #dogecoin\n\n$ Dollar: {prices[3]} Kč    #dollar\n€ Euro: {prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# History
def tweet_history(title, facts):
    if title == None or facts == None:
        pass
    else:
        fact = random.choice(facts)
        api.update_status(status = f"{title}\n\n{fact}\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nzdroj: https://wikipedia.cz\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# Latest YouTube video
def tweet_youtube(title, link):
    if title == None or link == None:
        pass
    else:
        api.update_status(status = f"Nové video na YouTube! 😍\n\n{title}\n{link}\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# Weather
def tweet_weather(emoji, date, temp, forecast):
    if date == None or temp == None or forecast == None:
        pass
    else:
        api.update_status(status = f"{date[0]} -> {temp[0]}°C ({forecast[0]} {emoji})\n{date[3]} -> {temp[3]}°C ({forecast[3]} {emoji})\n{date[7]} -> {temp[7]}°C ({forecast[7]} {emoji})\n{date[11]} -> {temp[11]}°C ({forecast[11]} {emoji})\n{date[15]} -> {temp[15]}°C ({forecast[15]} {emoji})\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()



### SCHEDULER ###
sched = BlockingScheduler()

# Currencies
@sched.scheduled_job('cron', hour='0,12')
def schedule_currencies():
    prices = fetch_currencies()
    tweet_currencies(prices)

# History
@sched.scheduled_job('cron', hour='20')
def schedule_history():
    title, facts = fetch_history()
    tweet_history(title, facts)

# YouTube
@sched.scheduled_job('cron', hour='15')
def schedule_youtube():
    title, link = fetch_youtube()
    tweet_youtube(title, link)

# Weather
@sched.scheduled_job('cron', hour='5')
def schedule_weather():
    emoji, date, temp, forecast = fetch_weather()
    tweet_weather(emoji, date, temp, forecast)

sched.start()
