"""Main module"""
import requests
from config import configure
from weather import Weather


def setup():
    """Setup function"""
    configure()
    session = requests.Session()
    city_name = input("Enter a city: ")
    weather_data = Weather.get_weather(session, city_name)
    Weather.display_weather(weather_data)


if __name__ == "__main__":
    setup()
