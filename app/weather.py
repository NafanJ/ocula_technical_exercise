import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"

def get_coordinates(city: str):
    response = requests.get(
        GEO_URL,
        params={
            "q": city,
            "limit": 1,
            "appid": API_KEY
        }
    )

    if response.status_code != 200 or not response.json():
        raise ValueError("City not found")

    data = response.json()[0]
    return data['lat'], data['lon']

def get_weather_data(city: str, target_date: str):
    # Get latitude and longitude for the city
    lat, lon = get_coordinates(city)

    # Convert target_date to a date object
    try:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    # Prepare the request URL
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "exclude": "current,minutely,hourly,alerts"
    }
    
    response = requests.get(WEATHER_URL, params=params)

    if response.status_code != 200:
        raise ValueError("Weather data unavailable")

    data = response.json()

    # Extract data for the specific day
    daily_data = data.get('daily', [])
    if not daily_data:
        raise ValueError("Weather data unavailable for the specified date")

    # Find the entry that matches the target date
    for entry in daily_data:
        entry_date = datetime.fromtimestamp(entry['dt']).date()
        if entry_date == target_date_obj:
            min_temp = round(entry['temp']['min'], 1)
            max_temp = round(entry['temp']['max'], 1)
            avg_temp = round((min_temp + max_temp) / 2, 1)
            humidity = round(entry['humidity'], 1)
            break
    else:
        raise ValueError("No matching data found for the specified date")

    return {
        "min_temp": min_temp,
        "max_temp": max_temp,
        "avg_temp": avg_temp,
        "humidity": humidity
    }
