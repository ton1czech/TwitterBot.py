# Import modules
import requests
import re
from bs4 import BeautifulSoup

# Get events from today's date in history
def get_history_events():
    global title, facts
    title = ''
    facts = []

    url = 'https://wikipedia.cz/'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'} 

    r = requests.get(url, headers=header).text
    soup = BeautifulSoup(r, 'lxml')

    table = soup.find('div', class_ = 'mainpage-block calendar-container')
    title = table.find('div', class_ = 'mainpage-headline').text
    events = table.find('ul').text
    events = events.splitlines()
    for event in events:
        event = re.sub('\(.+\)', '', event)
        event = re.sub('\s\.', '.', event)
        facts.append(event)

get_history_events()
