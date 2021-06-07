import requests
import re
from bs4 import BeautifulSoup

def fetch_history():
    facts = []

    url = 'https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana'

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    table = soup.find('div', class_ = 'mainpage-block calendar-container')
    title = table.find('div', class_ = 'mainpage-headline').text
    events = table.find('ul').text
    events = events.splitlines()
    for event in events:
        event = re.sub('\(.+\)', '', event)
        event = re.sub('\s\.', '.', event)
        facts.append(event)

    return title, facts