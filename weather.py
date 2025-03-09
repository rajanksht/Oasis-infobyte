import requests

def get_weather(location, api_key):
    """
    Fetch current weather data for the specified location using OpenWeatherMap API.
    The location can be a city name or a ZIP code.
    """
    # Determine whether the location is a ZIP code or a city name
    if location.isdigit():
        # Assuming country as US for ZIP code; adjust country code if needed
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") != 200:
            print("Error:", data.get("message", "Unable to fetch weather data."))
            return None
        
        weather_info = {
            "City": data.get("name"),
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Condition": data["weather"][0]["description"]
        }
        return weather_info
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    api_key = "94309cf27216a31da51f878efe8f7cee"  # Replace with your actual API key
    
    print("Welcome to the Basic Weather App!")
    location = input("Enter a city name or ZIP code: ").strip()
    
    weather = get_weather(location, api_key)
    if weather:
        print(f"\nWeather Information for {weather['City']}:")
        print(f"Temperature: {weather['Temperature']}°C")
        print(f"Humidity: {weather['Humidity']}%")
        print(f"Condition: {weather['Condition'].capitalize()}")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    main()
