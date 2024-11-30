# ========================================
# Daily Summary Addon
# ========================================

import os
import logging
import importlib.util
from pathlib import Path

# Utility function to dynamically discover addons and their capabilities
def discover_addons():
    """Scan the addons folder and return available modules."""
    base_dir = Path(__file__).parent.parent / "addons"
    if not base_dir.exists():
        logging.info("No addons folder found. Proceeding without addons.")
        return {}

    addons = {}
    for addon_file in base_dir.glob("*.py"):
        try:
            # Load the module dynamically
            spec = importlib.util.spec_from_file_location(addon_file.stem, addon_file)
            addon_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(addon_module)
            addons[addon_file.stem] = addon_module
        except Exception as e:
            logging.error(f"Error loading addon {addon_file.name}: {e}")
    return addons

# Fetch weather information if the weather addon is available
def fetch_weather(addons):
    weather_message = "Weather functionality is not available."
    for module_name, addon in addons.items():
        if hasattr(addon, "get_user_location") and hasattr(addon, "get_weather"):
            try:
                city, country = addon.get_user_location()
                if city and country:
                    return addon.get_weather(city, country)
                else:
                    return "Unable to determine your location for weather updates."
            except Exception as e:
                logging.error(f"Error in weather functionality from {module_name}: {e}")
                return "Weather functionality encountered an error."
    return weather_message

# Fetch stock market data if the stock market addon is available
def fetch_stock_market(addons):
    stock_message = "Stock market functionality is not available."
    for module_name, addon in addons.items():
        if hasattr(addon, "get_stock_market_overview"):
            try:
                return addon.get_stock_market_overview()
            except Exception as e:
                logging.error(f"Error in stock market functionality from {module_name}: {e}")
                return "Stock market functionality encountered an error."
    return stock_message

# Fetch news headlines
def fetch_news():
    """Fetch news headlines."""
    base_dir = Path(__file__).parent.parent / "API Keys"
    news_api_key_file = base_dir / "NewsAPI.txt"

    if not news_api_key_file.exists():
        return "News API key is missing. Please configure it in the API Keys folder."

    try:
        with open(news_api_key_file, "r") as f:
            api_key = f.read().strip()
            if not api_key or api_key == "YOUR_NEWSAPI_API_KEY_HERE":
                raise ValueError("Invalid News API key.")
    except Exception as e:
        logging.error(f"Error reading the News API key: {e}")
        return "Unable to fetch news due to missing API key."

    try:
        import requests
        base_url = "https://newsapi.org/v2/top-headlines"
        params = {"country": "us", "apiKey": api_key, "pageSize": 5}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        news_data = response.json()

        if news_data.get("status") != "ok":
            return "Unable to fetch news at this time."

        articles = news_data.get("articles", [])
        if not articles:
            return "No news articles available at the moment."

        news_summary = "\n".join(
            [f"- {article['title']}" for article in articles if article.get("title")]
        )
        return news_summary if news_summary else "No news articles available at the moment."
    except Exception as e:
        logging.error(f"Error fetching news data: {e}")
        return "Unable to fetch news at this time."

# Generate the daily summary
def generate_daily_summary():
    """Generate the daily summary by integrating with available addons."""
    userinfo_path = Path(__file__).parent.parent / "userinfo.txt"
    user_name = "User"
    try:
        with open(userinfo_path, "r") as f:
            user_name = f.read().strip()
    except FileNotFoundError:
        logging.warning("userinfo.txt not found. Using default name 'User'.")

    # Discover available addons
    addons = discover_addons()

    # Fetch components
    weather = fetch_weather(addons)
    stock_market = fetch_stock_market(addons)
    news = fetch_news()

    # Format the summary
    summary = f"Good morning, {user_name}!\n\n"
    summary += f"🌤 Weather: {weather}\n\n" if weather else ""
    summary += f"📈 Stock Market: {stock_market}\n\n" if stock_market else ""
    summary += f"📰 News Headlines:\n{news}\n\n"
    summary += "Have a great day ahead!"

    return summary

# Intent handler
def handle_daily_summary(user_input=None):
    return generate_daily_summary()

# Register the addon
def register(intent_handlers, intents, response_map):
    intents["daily_summary"] = [("summary", 3.0), ("daily", 2.5), ("today", 2.0)]
    response_map["daily_summary"] = ["Let me prepare your daily summary..."]
    intent_handlers["daily_summary"] = handle_daily_summary
