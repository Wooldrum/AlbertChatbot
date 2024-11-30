# ========================================
# Weather Addon
# ========================================

import os
import requests
import logging
import geocoder

# Dynamically locate the API Keys folder relative to the addons directory
base_dir = os.path.dirname(os.path.abspath(__file__))
api_keys_dir = os.path.join(base_dir, "..", "API Keys")
weather_api_key_file = os.path.join(api_keys_dir, "OpenWeatherAPIKey.txt")

# Ensure the API Keys folder and file exist
def ensure_api_key_file():
    if not os.path.exists(api_keys_dir):
        os.makedirs(api_keys_dir)
        logging.info(f"Created API Keys folder at {api_keys_dir}.")
    if not os.path.exists(weather_api_key_file):
        with open(weather_api_key_file, "w") as f:
            f.write("YOUR_OPENWEATHER_API_KEY_HERE")
        logging.info(f"Created OpenWeatherAPIKey.txt in {api_keys_dir}. Please add your API key.")

# Fetch the API key
def get_weather_api_key():
    ensure_api_key_file()
    try:
        with open(weather_api_key_file, "r") as f:
            api_key = f.read().strip()
            if api_key == "YOUR_OPENWEATHER_API_KEY_HERE" or not api_key:
                raise ValueError("Weather API key not configured.")
            return api_key
    except Exception as e:
        logging.error(f"Error reading the Weather API key: {e}")
        return None

# Get user location based on IP
def get_user_location():
    try:
        g = geocoder.ip("me")
        if g.ok:
            return g.city, g.country
        else:
            logging.error("Geocoder could not determine the location.")
            return None, None
    except Exception as e:
        logging.error(f"Error obtaining user location: {e}")
        return None, None

# Fetch weather data
def get_weather(city, country):
    api_key = get_weather_api_key()
    if not api_key:
        return "Weather API key is missing. Please configure it in the API Keys folder."

    if not city or not country:
        return "Unable to determine your location for weather updates."

    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": f"{city},{country}",
            "appid": api_key,
            "units": "imperial",
        }
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        weather_data = response.json()

        # Extract weather information
        description = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_info = (
            f"The current weather in {city}, {country} is {description} "
            f"with a temperature of {temperature}°F, humidity at {humidity}%, "
            f"and wind speed of {wind_speed} m/s."
        )
        return weather_info
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        return "Unable to fetch weather data at this time."

def handle_weather_intent(user_input=None):
    city, country = get_user_location()
    if not city or not country:
        return "Unable to determine your location for weather updates."
    return get_weather(city, country)

def register(intent_handlers, intents, response_map):
    intents["weather"] = [("weather", 2.5), ("forecast", 2.0), ("temperature", 1.5)]
    response_map["weather"] = ["Fetching the latest weather information..."]
    intent_handlers["weather"] = handle_weather_intent

# Ensure API Key file exists when loaded
ensure_api_key_file()
