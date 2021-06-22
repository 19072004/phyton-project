import requests
#import os
from datetime import datetime

api_key ='13d14ff2b23efc40ba0cf89a83f62e8e'
location = input("enter city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']))-273.15
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %y| %I:%M:%S %P")

print ("---------------------------------------------------------------")
print ("weather stats for - {} || {}".format(location.upper(), date_time))
print ("---------------------------------------------------------------")

print ("current temperature is: {:.2f} deg C".format(temp_city))
print ("current weather desc  :",weather_desc)
print ("current Humidity      :",hmdt, '%')
print ("current wind speed    :",wind_spd ,'kmph')
           
