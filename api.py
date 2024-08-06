import requests
from config import API_KEY



async def api_get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    res = requests.get(url).json()
    return res


