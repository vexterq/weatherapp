# WeatherApp - A simple weather information application

WeatherApp is a simple and easy to use weather information application that allows users to easily check current weather conditions for a specified city. It was developed using Python and the OpenWeatherMap API.

The application allows users to perform the following actions:

* Check current weather information for a specified city
* View temperature, humidity and wind speed
 
## Installation

To use WeatherApp, you will need to have Python 3 installed on your computer. You can download the latest version of Python from the official website.

You also need to sign up to OpenWeatherMap and get your own API key.

In addition, you will also need to install the following python packages:

* python-dotenv
* requests
You can install them by running the following command in your command prompt:

```bash
pip install -r requirements.txt
```
or
```bash
pip install python-dotenv requests
```

## Usage

To run the application, you need to insert your api_key to the api_key variable and specify city name in the city_name variable. Then navigate to the directory where the WeatherApp files are located and run the main.py file.

```bash
python main.py
```
You will be presented with the current weather information for the specified city.

## Requirements

* Python 3
* OpenWeatherMap API key
* python-dotenv
* requests
