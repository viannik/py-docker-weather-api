import os
import requests
import sys

def get_weather() -> None:
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': 'Paris',
        'aqi': 'no'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    location = data['location']
    current = data['current']

    print(f"Weather in {location['name']}, {location['country']}:")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['wind_kph']} km/h")


if __name__ == "__main__":
    get_weather()
