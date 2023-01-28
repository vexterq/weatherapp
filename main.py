from config import configure
import requests
from weather import Weather

if __name__ == "__main__":
    configure()
    s = requests.Session()
    city_name = input("Enter a city: ")
    weather_data = Weather.get_weather(s, city_name)
    Weather.display_weather(weather_data)
