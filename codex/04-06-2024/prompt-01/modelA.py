import requests

def get_weather(city_name, api_key, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=" + units
    response = requests.get(complete_url)

    if response.status_code == 200:  # Check for successful request
        data = response.json()
        weather = data['weather'][0]['description']  
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        return {
            'weather': weather,
            'temperature': temperature,
            'humidity': humidity
        }
    else:
        return None  # Indicate an error occurred

# Example Usage
my_api_key = "e7613c92b4a6e24ac4ad1689ddbb06a4" 
city = "London"

weather_data = get_weather(city, my_api_key)

if weather_data:
    print(f"Weather in {city}: {weather_data['weather']}")
    print(f"Temperature: {weather_data['temperature']} °C")
    print(f"Humidity: {weather_data['humidity']}%")
else:
    print("An error occurred fetching weather data.")