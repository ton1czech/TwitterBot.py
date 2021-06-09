import requests
from bs4 import BeautifulSoup

def fetch_sales():
    games = [[],[],[]]

    soup = BeautifulSoup(requests.get('https://gg.deals').text, 'lxml')
    column = soup.find_all('div', class_="list")[1]

    for id in range(0,10):
        game = column.find_all('div', class_="mainpage-preset-item")[id]

        title = game.find('a', class_="ellipsis title").text
        games[0].append(title)

        price = game.find('span', class_="numeric").text
        games[1].append(price)

        store = game.find('div', class_="tag-shop ellipsis tag with-bull").find('span', class_="value").text
        games[2].append(store)
    
    return games