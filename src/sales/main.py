import requests
import re
from bs4 import BeautifulSoup

def fetch_sales():
    url = 'https://gg.deals'

    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    
    column = soup.find_all('div', class_="list")[1]

    titles, prices, stores = [], [], []

    for id in range(0,10):
        game = column.find_all('div', class_="mainpage-preset-item")[id]

        title = game.find('a', class_="ellipsis title").text
        titles.append(title)

        price = game.find('span', class_="numeric").text
        prices.append(price)

        store = game.find('div', class_="tag-shop ellipsis tag with-bull")
        store = store.find('span', class_="value").text
        stores.append(store)
    
        if prices[id] != "Free":
            prices[id] = None
        
        print(prices)

    return titles, prices, stores

fetch_sales()