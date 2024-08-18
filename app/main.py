from fastapi import FastAPI, HTTPException
from app.models import WeatherResponse
from app.weather import get_weather_data

app = FastAPI()

@app.get("/weather", response_model=WeatherResponse)
async def weather(city: str, target_date: str):
    try:
        weather_data = get_weather_data(city, target_date)
        return WeatherResponse(
            city=city,
            min_temp=weather_data["min_temp"],
            max_temp=weather_data["max_temp"],
            avg_temp=weather_data["avg_temp"],
            humidity=weather_data["humidity"]
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
