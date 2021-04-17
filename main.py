# Import Modules
import tweepy
import pandas_datareader.data as data
import datetime as dt
import time
import schedule

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
    formatted = format(currency, ".3f")

# The actual tweet
def write_tweet(formatted):
    api.update_status(status = f"bitcoin: ${price[0]}    #bitcoin\nethereum: ${price[1]}    #ethereum\ndogecoin: ${price[2]}    #dogecoin\n\ndollar: {price[3]} kč    #dollar\neuro: {price[4]} kč    #euro\n\n\ntweet odeslal gingy, zabiják naprogramovanej borcem danečkem ❤\nsource code: https://github.com/ton1czech/gingy")

def test_tweet():
    api.update_status(status = f"heroku deploy test")

# Post the tweet everyday at same time
schedule.every().day.at("12:00").do(lambda: write_tweet(formatted))
schedule.every().day.at("21:28").do(test_tweet)
schedule.every().day.at("00:00").do(lambda: write_tweet(formatted))

while True:
    schedule.run_pending()
    time.sleep(1)