### IMPORT MODULES ###
import tweepy
import random
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from os import environ
from dotenv import load_dotenv

from currencies.main import fetch_currencies
from history_fact.main import fetch_history_fact
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



### CHECK FOR NONE IN DATA ###
def check(*args):
    for arg in args:
        if arg == None:
            sys.exit()
        if isinstance(arg, list) and None in arg:
            sys.exit()
        else:
            return args



### ACTUAL TWEETS ###
# Currencies
def tweet_currencies(prices):
    c_prices = check(prices)[0]
    api.update_status(status = f"Bitcoin: ${c_prices[0]}    #bitcoin\nEthereum: ${c_prices[1]}    #ethereum\nDogecoin: ${c_prices[2]}    #dogecoin\n\n$ Dollar: {c_prices[3]} Kč    #dollar\n€ Euro: {c_prices[4]} Kč    #euro\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# History
def tweet_history_fact(title, facts):
    c_title, c_fact = check(title)[0], random.choice(check(facts)[0])
    api.update_status(status = f"{c_title}\n\n{c_fact}\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\n\nzdroj: https://wikipedia.cz\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# YouTube 
def tweet_youtube(title, link):
    c_title, c_link = check(title)[0], check(link)[0]
    api.update_status(status = f"Nové video na YouTube! 😍\n\n{c_title}\n{c_link}\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
    sys.exit()

# Weather
def tweet_weather(emoji, date, temp, forecast):
    c_emoji, c_date, c_temp, c_forecast = check(emoji)[0], check(date)[0], check(temp)[0], check(forecast)[0]
    api.update_status(status = f"KLATOVY:\n\n{c_date[1]} -> {c_temp[1]}°C ({c_forecast[1]} {c_emoji[1]})\n{c_date[7]} -> {c_temp[7]}°C ({c_forecast[7]} {c_emoji[7]})\n{c_date[11]} -> {c_temp[11]}°C ({c_forecast[11]} {c_emoji[11]})\n{c_date[15]} -> {c_temp[15]}°C ({c_forecast[15]} {c_emoji[15]})\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")
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
def schedule_history_fact():
    title, facts = fetch_history_fact()
    tweet_history_fact(title, facts)

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
