import requests
import pandas as pd

api_key = input("Enter API key: ")
city = input('Enter City: ')
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(base_url)
data = response.json()


weather_info = {
    'city': data['name'],
    'weather' : data['weather'][0]["description"],
    'temperature' : data['main']['temp'],
    'feels like' : data ['main'] ["feels_like"],
    'temp min' : data ['main'] ['temp_min'],
    'temp max' : data ['main'] ['temp_max'], 
    'pressure' : data ['main'] ['pressure'],
    'humidity' : data ['main'] ['humidity'],
    'wind speed' : data ['wind'] ['speed'],
    'wind deg' : data ['wind'] ['deg']
}

df = pd.DataFrame([weather_info])

print(df)
