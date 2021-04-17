import pandas_datareader.data as data
import datetime as dt
import re

# Get real-time prices
price = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
for currency in price:
    formatted = format(currency, ".3f")
    print(currency)