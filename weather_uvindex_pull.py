'''
lat and long can be pulled from openweather api
website: https://www.openuv.io/dashboard?tab=0
'''


import requests
from Arc_today import *
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY_L&L")


# Example URL for getting UV index data from OpenUV API
url = "https://api.openuv.io/api/v1/uv"

# Set the latitude and longitude coordinates for the location you want
latitude = weather_data['coord']['lat']
longitude = weather_data['coord']['lon']


# Set the headers for the request, including your API key
headers = {
    "x-access-token": api_key
}

# Set the parameters for the request, including the latitude and longitude coordinates
params = {
    "lat": latitude,
    "lng": longitude
}

# Make the request and store the response as a dictionary
response = requests.get(url, headers=headers, params=params).json()

if __name__ == '__main__':
    pprint(response)
    print('-'*30)
    print(response)


# Extract the UV index value from the response dictionary
uv_index = response["result"]["uv"]


# COULD ALSO PULL OTHER DATA FROM THIS WEBSITE LIKE SUBRISE/SUNSET, GOLDENHOUR
if __name__ == '__main__':
    # Print the UV index value
    print(f"The UV index at ({latitude}, {longitude}) is {uv_index:.0f}")
