# Import Modules
import tweepy
import pandas_datareader.data as data
import datetime as dt
import schedule
import time
import re

# Set up Twitter API
with open('keys.txt') as f:
    content = f.read().splitlines()

consumer_key = content[0]
consumer_secret = content[1]
access_token = content[2]
access_token_secret = content[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get real-time prices
price = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
for currency in price:
    formatted = format(int(currency, ".3f"))
    formatted = format(formatted, ",")
    print(formatted)

# The actual tweet
# def write_tweet(formatted):
#     api.update_status(status = f"Bitcoin: ${price[0]}\nEthereum: ${price[1]}\nDogecoin: ${price[2]}\n\nDollar: {price[3]} Kč\nEuro: {price[4]} Kč\n\n\nTweet odeslal gingy, zabiják naprogramovanej borcem Danečkem ❤\nsource code: https://github.com/ton1czech/gingy")

# Post the tweet everyday at same time
# schedule.every().day.at("13:43").do(lambda: write_tweet(formatted))

while True:
    schedule.run_pending()
    time.sleep(1)