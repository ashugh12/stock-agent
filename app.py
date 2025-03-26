import os
import requests
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv


# Initialize FastAPI app
app = FastAPI()



# Load environment variables from .env file
load_dotenv()

# Fetch the API keys
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def fetch_stock_price(symbol):
    """Fetch latest stock price & previous close using Alpha Vantage API"""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"API Error: {response.status_code}")

    data = response.json().get("Time Series (Daily)", {})
    
    if not data:
        raise HTTPException(status_code=404, detail="Stock not found or API limit exceeded")
    
    # Get the latest two days' prices
    dates = sorted(data.keys(), reverse=True)
    latest_price = float(data[dates[0]]["4. close"])
    previous_price = float(data[dates[1]]["4. close"])

    return latest_price, previous_price

def analyze_stock(symbol, latest_price, previous_price):
    """Analyze stock trend & provide recommendation"""
    # Determine trend
    trend = "rising" if latest_price > previous_price else "falling"
    
    # AI-enhanced recommendation
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"The stock {symbol} has a current price of {latest_price} and was {previous_price} yesterday. "
        f"It is currently {trend}. Should an investor buy, sell, or hold? Provide a brief reason."
    )
    
    response = model.generate_content(prompt)
    return trend, response.text.strip()


@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    """Fetch stock price, analyze trend, and provide recommendation"""
    latest_price, previous_price = fetch_stock_price(symbol.upper())
    trend, recommendation = analyze_stock(symbol.upper(), latest_price, previous_price)

    return {
        "stock": symbol.upper(),
        "latest_price": latest_price,
        "previous_price": previous_price,
        "trend": trend,
        "recommendation": recommendation
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "API is running"}