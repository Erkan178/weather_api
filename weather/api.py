import requests
import logging

# Loglama yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')

API_KEY = '0159de0998664cadab751149250402'
BASE_URL = 'http://api.weatherapi.com/v1/forecast.json'

def get_weather(city):
    params = {
        'q': city,
        'key': API_KEY,
        'days': 3,
        'aqi': 'no'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
