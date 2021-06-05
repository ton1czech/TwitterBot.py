# Import modules
import requests
from os import environ
from dotenv import load_dotenv
from datetime import datetime

from pprint import pprint

load_dotenv()

lat = 49.395555
lon = 13.295094
drop = 'current,minutely,daily,alerts'
units = 'metric'
lang = 'cz'

# Get weather forecast in Klatovy for today
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={drop}&units={units}&lang={lang}&appid={environ['API_key']}"
    weather = requests.get(url).json()

    date = weather['hourly'][0]['dt']
    date = datetime.fromtimestamp(date).strftime("%H")

    temp = weather['hourly'][0]['temp']
    print(temp)

get_weather()
