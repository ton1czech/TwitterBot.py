import pandas_datareader.data as data

def fetch_currencies():
    currencies = data.get_quote_yahoo(['BTC-USD', 'ETH-USD', 'DOGE-USD', 'CZK=X', 'EURCZK=X'])['price']
    prices = [format(currency, ",.3f") for currency in currencies]      # store all currencies inside list

    return prices