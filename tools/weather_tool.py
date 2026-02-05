import requests
import os
import time

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str, retries=2):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    for _ in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"]
            }
        time.sleep(1)

    raise Exception("Weather API failed")
