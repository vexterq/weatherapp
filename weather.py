"""This module contains the Weather class."""
import os


class Weather:
    """This class contains the methods to get and display weather data."""
    @staticmethod
    def get_weather(session, city_name):
        """This method gets the weather data.
                Args:
                    session: The requests session.
                    city_name: The name of the city."""

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={os.getenv('api_key')}"
        response = session.get(url)
        return response.json()

    @staticmethod
    def display_weather(weather_data):
        """This method displays the weather data.
                Args:
                    weather_data: The weather data."""
        print(
            f'Weather in {weather_data["name"]}, {weather_data["sys"]["country"]}:')
        print(
            f'{weather_data["weather"][0]["main"]}☁️, {weather_data["weather"][0]["description"]}')
        print(f'Temperature🌡️: {weather_data["main"]["temp"]}°C')
        print(f'Humidity💧: {weather_data["main"]["humidity"]}%')
        print(f'Wind💨: {weather_data["wind"]["speed"]}m/s')
