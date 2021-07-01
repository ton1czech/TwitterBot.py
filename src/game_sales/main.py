import requests
from bs4 import BeautifulSoup

def fetch_game_sales():
    games = [[],[],[]]

    soup = BeautifulSoup(requests.get('https://gg.deals').text, 'lxml')
    column = soup.find_all('div', class_="list")[1]

    for id in range(0,10):
        game = column.find_all('div', class_="mainpage-preset-item")[id]

        title = game.find('a', class_="ellipsis title").text
        price = game.find('span', class_="numeric").text
        store = game.find('div', class_="tag-shop ellipsis tag with-bull").find('span', class_="value").text

        if price == "Free":
            games[0].append(title)
            games[1].append(price)
            games[2].append(store)

    return games