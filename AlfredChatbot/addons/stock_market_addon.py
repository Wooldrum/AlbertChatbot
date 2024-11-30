# ========================================
# Stock Market Addon
# ========================================

import yfinance as yf
import logging

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            return f"The current price of {ticker.upper()} is ${current_price:.2f}."
        else:
            return f"Data not available for {ticker.upper()}."
    except Exception as e:
        logging.error(f"Error fetching stock data: {e}")
        return "Sorry, I couldn't retrieve the stock data at this time."

def get_stock_market_overview():
    try:
        # Fetch data for major indices
        indices = {
            'S&P 500': '^GSPC',
            'Dow Jones Industrial Average': '^DJI',
            'NASDAQ Composite': '^IXIC',
        }
        overview = "Here's the current status of major indices:\n"
        for name, ticker in indices.items():
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                change = hist['Close'].iloc[-1] - hist['Open'].iloc[-1]
                change_percent = (change / hist['Open'].iloc[-1]) * 100
                overview += f"- {name} ({ticker}): {current_price:.2f} ({change:+.2f}, {change_percent:+.2f}%)\n"
            else:
                overview += f"- {name}: Data not available.\n"
        return overview.strip()
    except Exception as e:
        logging.error(f"Error fetching stock market overview: {e}")
        return "Sorry, I couldn't retrieve the stock market data at this time."

def handle_stock_prices(user_input):
    print("Chatbot: Please enter the company's ticker symbol (e.g., AAPL for Apple):")
    ticker = input("You: ").strip().upper()
    return get_stock_price(ticker)

def handle_stock_market_overview(user_input):
    return get_stock_market_overview()

def register(intent_handlers, intents, response_map):
    # Register stock price intent
    intents["stock_prices"] = [
        ("stock", 2.0),
        ("price", 1.5),
        ("stock price", 3.0),
        ("price of stock", 3.0),
        ("stock of", 2.0),
        ("stock price of", 3.0),
        ("company stock", 2.5),
        ("share price", 2.5),
        ("stock quote", 2.5),
        ("quote of", 2.0),
        ("ticker", 2.0),
    ]
    response_map["stock_prices"] = ["Let me fetch that stock price for you!"]
    intent_handlers["stock_prices"] = handle_stock_prices

    # Register stock market overview intent
    intents["stock_market_overview"] = [
        ("stock market", 3.0),
        ("market", 2.0),
        ("how are stocks", 2.5),
        ("how is the market", 2.5),
        ("stocks doing", 2.5),
        ("market today", 2.5),
        ("market update", 2.5),
        ("stock indices", 2.5),
        ("how are the stocks", 2.5),
        ("stock market today", 3.0),
        ("market performance", 2.5),
    ]
    response_map["stock_market_overview"] = ["Fetching the current stock market overview..."]
    intent_handlers["stock_market_overview"] = handle_stock_market_overview

    # Update common phrases if necessary
    # common_phrases.update({
    #     "how are stocks doing": "stock_market_overview",
    #     "how is the stock market": "stock_market_overview",
    # })

# Note: No need to define 'custom_analyze_user_input' here, as we're relying on the default or other addons.
