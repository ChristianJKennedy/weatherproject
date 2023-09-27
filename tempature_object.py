'''
- Possibly turn precipitation into an object, or within the object have methods with return statements.
'''

from Arc_today import *
from weather_uvindex_pull import *

# create a weather class that includes all general weather information
# after weather class created, create child subclasses to extract specific weather data depending upon what the user
# cares about
class Weather:
    def __init__(self, city_name, fahrenheit_temp, humidity, wind_speed, description, uv_index):
        self.city = city_name
        self.temp = fahrenheit_temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.description = description
        self.uv_index = uv_index

    def __str__(self):
        return f'City name: {self.city}\n' \
               f'Temperature: {self.temp:.0f} F\n' \
               f'Humidity: {self.humidity}%\n' \
               f'Wind speed: {self.wind_speed} m/s\n' \
               f'Description: {self.description}\n' \
               f'UV index: {self.uv_index:.0f}'

class Precipiation(Weather):
    def __init__(self, fahrenheit_temp, humidity, description):
        self.temp = fahrenheit_temp
        self.humidity = humidity
        self.description = description

    def precip(self):
        if 'rain' in description:
            print('It is raining, wear your rain jacket.')

    def __str__(self):
        return f'{description}'
'''
NEXT STEPS HERE'''
# figure out a way to create multiple instances  to pull weather data from multiple cities
# Maybe put user input into this module for each instance


t1 = Weather(city_name,
             fahrenheit_temp,
             humidity,
             wind_speed,
             description,
             uv_index)

t2 = Weather(city_name, fahrenheit_temp, humidity, wind_speed, description, uv_index)

#test cases
#print(t1, f'\n', '-'*20, f'\n', t2)
#print('-'*50)

p1 = Precipiation(fahrenheit_temp, humidity, description)
#print(p1)