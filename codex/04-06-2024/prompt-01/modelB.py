import requests

api_key = "e7613c92b4a6e24ac4ad1689ddbb06a4"
base_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = "London"
units = "metric" # for Celsius, use imperial for Fahrenheit

# Build the full URL with query parameters
url = f"{base_url}?q={city_name}&appid={api_key}&units={units}"

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Extract the required data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    
    print(f"Temperature in {city_name}: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")
else:
    print("Error:", response.status_code)