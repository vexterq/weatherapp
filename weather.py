import os


class Weather:
    @staticmethod
    def get_weather(session, city_name):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={os.getenv('api_key')}"
        response = session.get(url)
        return response.json()

    def display_weather(weather_data):
        print(
            f'Weather in {weather_data["name"]}, {weather_data["sys"]["country"]}:')
        print(
            f'{weather_data["weather"][0]["main"]}☁️, {weather_data["weather"][0]["description"]}')
        print(f'Temperature🌡️: {weather_data["main"]["temp"]}°C')
        print(f'Humidity💧: {weather_data["main"]["humidity"]}%')
        print(f'Wind💨: {weather_data["wind"]["speed"]}m/s')
