# Program to check weather and return with arcteryx shall be worn
'''
website: https://openweathermap.org
'''
# import requests to request data
import requests

# pprint allows data to be printed in an orderly easy to read format
from pprint import pprint

# API key
API_Key = 'a04d436a3b9650b4d9c365c734a2c8a4'

# city user input
# print('Are we going to be arc\'d up today?')
city = 'memphis' # input('Enter your city: ')

# Url to pull data
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_Key+'&q='+city

# pull data from url and format into json file
weather_data = requests.get(base_url).json()


# Extract the key values you want from the dictionary
city_name = weather_data['name']
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']

# convert temp in kelvin to degrees fahrenheit
celsius_temp = temperature - 273.15
fahrenheit_temp = celsius_temp * 9 / 5 + 32


if __name__ == '__main__':
    # Prints weather data in a easier to read format
    pprint(weather_data)
    print('-'*20)

    # convert temp in kelvin to degrees fahrenheit
    celsius_temp = temperature - 273.15
    fahrenheit_temp = celsius_temp * 9/5 + 32
    print(f"The temperature {temperature} K is equivalent to {fahrenheit_temp:.2f} °F")

    # Print the extracted values
    print(f"City name: {city_name}")
    print(f"Temperature: {fahrenheit_temp:.0f} F")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
    print(f"Description: {description}")










