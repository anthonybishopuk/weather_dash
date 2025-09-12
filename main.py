import pandas
import matplotlib
from data import get_weather, parse_weather, insert_weather


if __name__ == "__main__":
    cities = ["London", "Paris", "New York", "Tokyo", "Sydney"]

    for city in cities:
        data = get_weather(city)
        record = parse_weather(data, city)
        insert_weather(record)
        print(f"Inserted weather for {city}")
    