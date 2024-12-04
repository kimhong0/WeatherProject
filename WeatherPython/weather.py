import requests
from datetime import datetime, timedelta

# API Key and URL
API_KEY = "3f16fd3ce60503799506204de7830cfe"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    """
    Fetch weather data for a given city.
    
    Args:
        city (str): The name of the city to fetch weather for.

    Returns:
        dict: A dictionary containing weather details or an error message.
    """
    try:
        # Make an API request
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data = response.json()

        if data["cod"] != 200:
            return {"error": "City not found"}

        # Extract weather data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        timezone_offset = data["timezone"]

        # Calculate city time
        utc_time = datetime.utcnow()
        city_time = utc_time + timedelta(seconds=timezone_offset)
        formatted_time = city_time.strftime("%I:%M %p")

        return {
            "city": f"{city_name}, {country}",
            "time": formatted_time,
            "temperature": f"{int(temp)}°",
            "feels_like": f"Feels like {int(feels_like)}°",
            "description": description,
            "wind_speed": f"{wind_speed} m/s",
            "humidity": f"{humidity} %",
            "pressure": f"{pressure} hPa",
        }

    except Exception as e:
        return {"error": str(e)}
