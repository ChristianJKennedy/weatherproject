# Program to check weather and return with rain jacket should be worn
'''
website: https://openweathermap.org
'''
# import requests to request data
import requests

# pprint allows data to be printed in an orderly easy to read format, import dotenv file to access API_KEY
from pprint import pprint
import os
from dotenv import load_dotenv
import pandas as pd

# Load the .env file
load_dotenv()

# Access the API key
API_Key = os.getenv("API_KEY")

'''Update: Gather user data put in arc_today rather than main file to gather user input city'''
# public google sheet url
SHEET_ID = '10_CZKmK5q0CQjwvGMmm31Cciy3QfnZy-eZAl42MAlqI'
SHEET_NAME = 'Sheet1'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

# Create function for data framework
def load_df(url):
    today_date = ['date', 'notifications_yn']
    df = pd.read_csv(url, parse_dates=today_date)
    return df

# function to isolate city from df
def user_city(df):
    for _, row in df.iterrows():
        city = row['city']
    return city

# gather data framework for user data
df = load_df(URL)
city = user_city(df)

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

    print(df)
    print(city)









