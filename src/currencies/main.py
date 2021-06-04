# Import modules
import pandas_datareader.data as data

# Get real-time prices of currencies
prices = []

def get_prices():
    price = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
    for currency in price:
        currency = format(currency, ",.3f")
        prices.append(currency)

get_prices()