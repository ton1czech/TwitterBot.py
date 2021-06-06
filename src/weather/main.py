# Import modules
import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

lat = 49.395555
lon = 13.295094
drop = 'current,minutely,daily,alerts'
units = 'metric'
lang = 'cz'

# Get weather forecast in Klatovy for today
def fetch_weather():
    global emoji, date, temp, forecast
    emoji, date, temp, forecast = '', [], [], []

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={drop}&units={units}&lang={lang}&appid={environ['API_key']}"
    weather = requests.get(url).json()

    for id in range(0,20):
        date.append(datetime.fromtimestamp(weather['hourly'][id]['dt']).strftime("%H:%M"))
        temp.append(weather['hourly'][id]['temp'])
        forecast.append(weather['hourly'][id]['weather'][0]['description'])
    
    # emoji generator
    st = weather['hourly'][id]['weather'][0]['description']
    if st  == "déšť":
        emoji = '☔'
    elif st == "slabý déšť":
        emoji = '🌧'
    elif st == 'zataženo':
        emoji = '☁'
    elif st == 'oblačno':
        emoji = '⛅'
    else:
        emoji = '❓'
    
    return emoji, date, temp, forecast