import requests
import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

weather_api = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    
    response = requests.get(weather_api, params=params)
    
    if response.status_code != 200:
        print(response.text)
    else:
        return response.json()

def parse_weather(data, city):
        return (
            city,
            data["sys"]["country"],
            datetime.fromtimestamp(data["dt"]).isoformat(),
            data["main"]["temp"],
            data["main"]["humidity"],
            data["weather"][0]["description"],
            data["wind"]["speed"]
        )

def insert_weather(record):
    conn = sqlite3.connect("data/weather.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO weather (city, country, date_time, temperature, humidity, description, wind_speed)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, record)
    conn.commit()
    conn.close()