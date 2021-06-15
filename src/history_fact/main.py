import requests
import re
from bs4 import BeautifulSoup

def fetch_history_fact():
    facts = []

    soup = BeautifulSoup(requests.get('https://wikipedia.cz').text, 'lxml')

    table = soup.find('div', class_ = 'mainpage-block calendar-container')
    title = table.find('div', class_ = 'mainpage-headline').text
    events = table.find('ul').text
    events = events.splitlines()
    for event in events:
        event = re.sub('\s\(.+\)', '', event)
        facts.append(event)

    return title, facts