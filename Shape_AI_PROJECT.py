import requests
from datetime import datetime

api_key = '0df7671a277067f89d72939aef0c878d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('weather.txt', 'w') as file:
    file.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
    file.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
    file.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
    file.write("Current weather desc  : "+weather_desc+"\n")
    file.write("Current Humidity      : "+str(hmdt)+'% \n')
    file.write("Current wind speed    : "+str(wind_spd)+'kmph \n')
