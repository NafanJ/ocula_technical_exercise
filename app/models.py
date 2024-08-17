from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    min_temp: float
    max_temp: float
    avg_temp: float
    humidity: float
