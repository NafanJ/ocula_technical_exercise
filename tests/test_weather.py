import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Unit Test: Weather GET endpoint
def test_weather_endpoint():
    response = client.get("/weather?city=London&target_date=2024-08-19")
    assert response.status_code == 200
    data = response.json()
    assert "min_temp" in data
    assert "max_temp" in data
    assert "avg_temp" in data
    assert "humidity" in data

# Unit Test: Invalid city name
def test_weather_invalid_city():
    response = client.get("/weather?city=InvalidCity&target_date=2024-08-19")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "City not found"

# Edge case: Empty city parameter
def test_weather_empty_city():
    response = client.get("/weather?city=&target_date=2024-08-19")
    assert response.status_code == 404

# Edge case: Very large input
def test_weather_large_city_name():
    large_city_name = "A" * 300
    response = client.get(f"/weather?city={large_city_name}&target_date=2024-08-19")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "City not found"

# Edge case: Special characters in city name
def test_weather_special_characters_city():
    special_char_city = "@!#$$%"
    response = client.get(f"/weather?city={special_char_city}&target_date=2024-08-19")
    assert response.status_code == 422

# Edge case: Target date outside 7-day range
def test_weather_invalid_target_date():
    response = client.get("/weather?city=London&target_date=2024-08-15")
    assert response.status_code == 404

# Edge case: Empty target_date parameter
def test_weather_empty_target_date():
    response = client.get("/weather?city=London")
    assert response.status_code == 422