#!/usr/bin/env python

# Config

###########################################################################################################################

api_key = "changeme" # Create an account on OpenWeather (it's free) and get your API token there
city = "changeme" # Your city                                                                                                 
units = "metric" # you can choose metric or imperial                                                                      
timeplus = "0" # Timezone used by default is UTC/GMT so you can define how many hours should be added to the time         
timeminus = "0" # Timezone used by default is UTC/GMT so you can define how many hours should be subtracted from the time 

###########################################################################################################################

import requests
import datetime
import sys

timeplus = int(timeplus)
timeminus = int(timeminus)

if units == "metric":
    windspeedunits = "m/s"
elif units == "imperial":
    windspeedunits = "mph"
else:
    windspeedunits = "m/s"

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&APPID={api_key}")

if weather_data.json() ['cod'] == 200:
    pass
elif weather_data.json() ['cod'] == '404':
    print("No city found")
    sys.exit()
elif weather_data.json() ['cod'] == 401:
    print("Invalid API key")
    sys.exit()
else:
    print("Unknown error occured.")
    sys.exit()

sourcesunrise = weather_data.json()['sys']['sunrise']
sourcesunset = weather_data.json()['sys']['sunset']

sunrise_datetime = datetime.datetime.utcfromtimestamp(sourcesunrise)
sunset_datetime = datetime.datetime.utcfromtimestamp(sourcesunset)

adjusted_sunrise = sunrise_datetime + datetime.timedelta(hours=timeplus) - datetime.timedelta(hours=timeminus)
adjusted_sunset = sunset_datetime + datetime.timedelta(hours=timeplus) - datetime.timedelta(hours=timeminus)

sunrisestring = adjusted_sunrise.strftime("%H:%M:%S")
sunsetstring = adjusted_sunset.strftime("%H:%M:%S")

weather = weather_data.json()['weather'][0]['main']

temp = str(round(weather_data.json()['main']['temp'])) + '°'

if units == "metric":
    temp += " C"
else:
    temp += " F"

wind_speed = str(round(weather_data.json()['wind']['speed']))

if weather == "Clear":
    print("     \   /     " + "Weather: clear", 
          "      .-.      " + "Temperature: " + temp, 
          "   ‒ (   ) ‒   " + "Wind speed: " + wind_speed + " " + windspeedunits,
          "      `-᾿      " + "Sunrise: " + sunrisestring, 
          "     /   \     " + "Sunset: " + sunsetstring, 
          "               ", sep = '\n')
elif weather == "Clouds":
    print("                 " + "Weather: cloudy", 
          "       .--.      " + "Temprature: " + temp, 
          "    .-(    ).    " + "Wind speed: " + wind_speed + " " + windspeedunits, 
          "   (___.__)__)   " + "Sunrise: " + sunrisestring,
          "                 " + "Sunset: " + sunsetstring,
          "                 ", sep = '\n')
elif weather == "Rain":
    print("                 " + "Weather: rainy", 
          "       .--.      " + "Temprature: " + temp, 
          "    .-(    ).    " + "Wind speed: " + wind_speed + " " + windspeedunits, 
          "   (___.__)__)   " + "Sunrise: " + sunrisestring,
          "    ʻ‚ʻ‚ʻ‚ʻ‚ʻ    " + "Sunset: " + sunsetstring,
          "                 ", sep = '\n')
elif weather == "Snow":
    print("                 " + "Weather: snowy", 
          "       .--.      " + "Temprature: " + temp, 
          "    .-(    ).    " + "Wind speed: " + wind_speed + " " + windspeedunits, 
          "   (___.__)__)   " + "Sunrise: " + sunrisestring,
          "    * * * * *    " + "Sunset: " + sunsetstring,
          "                 ", sep = '\n')
elif weather == "Thunderstorm":
    print("       .--.      " + "Weather: stormy", 
          "    .-(    ).    " + "Temprature: " + temp, 
          "   (___.__)__)   " + "Wind speed: " + wind_speed + " " + windspeedunits, 
          "        /_       " + "Sunrise: " + sunrisestring,
          "         /       " + "Sunset: " + sunsetstring,
          "                 ", sep = '\n')
else:
    print("                 " + "Weather: " + weather, 
          "       .--.      " + "Temprature: " + temp, 
          "    .-(    ).    " + "Wind speed: " + wind_speed + " " + windspeedunits, 
          "   (___.__)__)   " + "Sunrise: " + sunrisestring,
          "                 " + "Sunset: " + sunsetstring,
          "                 ", sep = '\n')
