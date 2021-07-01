import requests

def fetch_nameday():
    response = requests.get("https://svatky.adresa.info/json")

    name = response.json()[0]['name']

    return name