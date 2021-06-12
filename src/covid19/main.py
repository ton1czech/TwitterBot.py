import requests

def fetch_covid19():
    r = requests.get("https://disease.sh/v3/covid-19/all").json()
    today_cases, today_recovered, today_deaths = r["todayCases"], r["todayRecovered"], r["todayDeaths"]

    return today_cases, today_recovered, today_deaths

fetch_covid19()