# Import Modules
import tweepy
import pandas_datareader.data as data
import datetime as dt

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

# The actual tweet
api.update_status(status = f"""
Bitcoin: {price[0]} $
Ethereum: {price[1]} $
Dogecoin: {price[2]} $

Dollar: {price[3]} Kč
Euro: {price[4]} Kč
""")