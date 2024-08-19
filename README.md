
# Weather API Project

This project is a FastAPI-based web application that retrieves weather data for a given city and date, and returns the minimum, maximum, and average temperatures, along with the humidity. The weather data is fetched from the OpenWeatherMap API.

## Features

- **GET /weather**: Retrieve weather data (minimum, maximum, average temperature, and humidity) for a specified city and day.
- **Environment Variable Configuration**: The API key for OpenWeatherMap is securely managed through environment variables.
- **Unit Testing**: The application includes unit tests to ensure the functionality of the API endpoints.
- **CI/CD**: Github Actions has been utilised to ensure continuous testing and deployment.

## Live Demo
A live version of this API is deployed on AWS Elastic Beanstalk.
### Example Usage
To get the weather data for London on 24th August 2024:
```bash
http://openweathermap-env.eba-2jrahwga.us-east-1.elasticbeanstalk.com/weather?city=London&target_date=2024-08-24
```

## Project Structure

```
ocula_technical_exercise/
│
├── .github/
│   ├── workflows/
│      ├── weather-app.yml # Github Actions CI/CD
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application and API endpoint definitions
│   └── weather.py         # Functions to get and process weather data
│   └── models.py          # API Response Schemas
├── tests/
│   ├── __init__.py
│   └── test_weather.py    # Tests for the API endpoints
├── .gitignore             # Ignore unnecessary files in version control
├── Procfile               # ElasticBeanstalk FastAPI Configuration
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables (not included in version control)
```

## Getting Started

### Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)
- **OpenWeatherMap API Key**

### Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:NafanJ/ocula_technical_exercise.git
   cd ocula_technical_exercise
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root of the project and add your OpenWeatherMap API key:

   ```plaintext
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

### Running the Application

To run the FastAPI application locally:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### API Usage

- **GET /weather**: Retrieve weather data for a specific city on a date.
  **Query Parameters:**
  - `city` (required): The name of the city for which you want to retrieve weather data.
  - `target_date` (required): The date for which you want to retrieve weather data in the format `YYYY-MM-DD`.


  **Example Request:**

  ```
  GET /weather?city=London&target_date=2024-08-19
  ```

  **Example Response:**

  ```json
  {
      "city": "London",
      "min_temp": 12.34,
      "max_temp": 18.56,
      "avg_temp": 15.45,
      "humidity": 77
  }
  ```

### Running Tests

To run the tests for this project, use `pytest`:

```bash
pytest
```

This will run all the unit tests located in the `tests` directory.

### Environment Variables

- `OPENWEATHERMAP_API_KEY`: Your API key from OpenWeatherMap to access weather data.
