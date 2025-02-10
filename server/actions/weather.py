import os
from datetime import datetime
import requests


# Function to Get Weather from a Location or W/O Location
def get_weather(entities: list = []) -> dict:
    location = os.getenv("USER_CITY")

    # Set the value of location entity
    for entity in entities:
        if entity["name"] == "location":
            location = entity["value"]
            break

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={os.getenv("OPEN_WEATHER_APPID")}"
    ).json()

    location = response["name"]
    description = response["weather"][0]["description"].capitalize()
    temp_celsius = round(response["main"]["temp"] - 273.15, 1)

    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]
    sunrise = datetime.fromtimestamp(response["sys"]["sunrise"]).strftime("%I:%M %p")
    sunset = datetime.fromtimestamp(response["sys"]["sunset"]).strftime("%I:%M %p")

    return_response = {
        "key": "SPEAK",
        "perform": "text_processing",
        "text": (
            f"The weather in {location} is currently {description} with a temperature of {temp_celsius}°C. "
            f"Humidity is at {humidity}% and wind speed is {wind_speed} m/s. "
            f"Sunrise was at {sunrise} and sunset will be at {sunset}."
        ),
    }

    return return_response
