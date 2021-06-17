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

def fetch_weather():
    emoji, date, temp, forecast = [], [], [], []

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={drop}&units={units}&lang={lang}&appid={environ['openweathermap_key']}"
    weather = requests.get(url).json()

    for id in range(0,20):
        date.append(datetime.fromtimestamp(weather['hourly'][id]['dt']).strftime("%H:%M"))
        temp.append(weather['hourly'][id]['temp'])
        forecast.append(weather['hourly'][id]['weather'][0]['description'])

        # emoji generator
        if forecast[id]  == "déšť":
            emoji.append('☔')
        elif forecast[id] == "slabý déšť":
            emoji.append('🌧')
        elif forecast[id] == "zataženo":
            emoji.append('☁')
        elif forecast[id] == "oblačno":
            emoji.append('⛅')
        elif forecast[id] == "jasno":
            emoji.append('☀')
        elif forecast[id] == "polojasno":
            emoji.append('🌥')
        elif forecast[id] == "skoro jasno":
            emoji.append('🌤')
        else:
            emoji.append('❓')
    
    return emoji, date, temp, forecast