import requests
from bs4 import BeautifulSoup

def fetch_game_sales():
    games = [[],[],[]]

    soup = BeautifulSoup(requests.get('https://gg.deals').text, 'lxml')
    column = soup.find_all('div', class_="list")[1]

    for id in range(0,10):
        game = column.find_all('div', class_="mainpage-preset-item")[id]

        games[0].append(game.find('a', class_="ellipsis title").text)   # title
        games[1].append(game.find('span', class_="numeric").text)       # price
        games[2].append(game.find('div', class_="tag-shop ellipsis tag with-bull").find('span', class_="value").text) # store
    
    return games