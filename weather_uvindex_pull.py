'''
lat and long can be pulled from openweather api
website: https://www.openuv.io/dashboard?tab=0
'''


import requests
from Arc_today import *

# Example URL for getting UV index data from OpenUV API
url = "https://api.openuv.io/api/v1/uv"

# Set the latitude and longitude coordinates for the location you want
latitude = weather_data['coord']['lat']
longitude = weather_data['coord']['lon']

# Set the headers for the request, including your API key
headers = {
    "x-access-token": "openuv-180e7rlhl4dybf-io"
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

# COULD ALSO PULL OTHER DATA FROM THIS WEBSITE LIKE SUBRISE/SUNSET, GOLDENHOUR, BEST TIME TO TAN

if __name__ == '__main__':
    # Print the UV index value
    print(f"The UV index at ({latitude}, {longitude}) is {uv_index:.0f}")
