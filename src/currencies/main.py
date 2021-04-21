# Get real-time prices
prices = []

def get_prices(data):
    price = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
    for currency in price:
        currency = format(currency, ",.3f")
        prices.append(currency)