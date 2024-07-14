import requests
import pandas as pd


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)



def fetch_weather_data(city, api_key):
    base_url = f'http://api.openWeathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(base_url)
        response.raise_for_status
        data = response.json()

        if 'name' not in data or 'weather' not in data:
            raise ValueError('Invalid response received from API. Please check the city name.')

        weather_info = {
            "City": data["name"],
            "Weather": data["weather"][0]["description"],
            "Temperature (F)": kelvin_to_fahrenheit(data["main"]["temp"]),  # Convert Kelvin to Fahrenheit
            "Feels Like (F)": kelvin_to_fahrenheit(data["main"]["feels_like"]),
            "Temp Min (F)": kelvin_to_fahrenheit(data["main"]["temp_min"]),
            "Temp Max (F)": kelvin_to_fahrenheit(data["main"]["temp_max"]),
            "Pressure (hPa)": data["main"]["pressure"],
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"],
            "Wind Direction (deg)": data["wind"]["deg"]
        }

        df = pd.DataFrame([weather_info])
        return df
    
    except requests.HTTPError as http_err:
        if response.status_code == 401:
            print("Invalid API key. Please try again.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except requests.RequestException as e:
        print(f"Error fetching data from OpenWeatherMap API: {e}")
        return None  # Return None in case of error
    except ValueError as ve:
        print(ve)
        return None  # Return None in case of invalid response

    

while True:
    api_key = input("Enter your OpenWeatherMap API key: ")
    if fetch_weather_data("London", api_key) is not None:
        break
    else:
        print("Invalid API key. Please try again.")

while True:
    city = input("Enter a city: ")
    weather_df = fetch_weather_data(city, api_key)
    if weather_df is not None:
        print(weather_df)
        break
    else:
        print("Please enter a valid city name.")
    