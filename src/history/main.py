# Import modules
import requests
from bs4 import BeautifulSoup

# Get events from today's date in history
def get_history_events():
    global title, facts

    url = 'https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'} 

    r = requests.get(url, headers=header).text
    soup = BeautifulSoup(r, 'lxml')

    table = soup.find('div', class_ = 'mainpage-block calendar-container')
    title = table.find('div', class_ = 'mainpage-headline').text
    facts = table.find('ul').text

get_history_events()