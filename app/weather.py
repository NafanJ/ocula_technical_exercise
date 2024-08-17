import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str):
    response = requests.get(
        BASE_URL,
        params={
            "q": city,
            "units": "metric",
            "appid": API_KEY
        }
    )

    if response.status_code != 200:
        raise ValueError("City not found or weather data unavailable")

    data = response.json()

    # Extract temperature and humidity data from the response
    min_temp = round(data['main']['temp_min'], 1)
    max_temp = round(data['main']['temp_max'], 1)
    avg_temp = round((min_temp + max_temp) / 2, 1)
    humidity = round(data['main']['humidity'], 1)

    return {
        "min_temp": min_temp,
        "max_temp": max_temp,
        "avg_temp": avg_temp,
        "humidity": humidity
    }
