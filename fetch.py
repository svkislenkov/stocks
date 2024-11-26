import requests

from config import API_KEY

def fetch_data(ticker, date):
    """Fetch daily data for a specific stock for a specific date"""
    url =f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{date}/{date}?adjusted=true&sort=asc&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed."}
    
def fetch_ma(ticker, window):
    """Fetch moving average information"""
    
    url = f'https://api.polygon.io/v1/indicators/sma/{ticker}?timespan=week&adjusted=true&window={window}&series_type=close&order=desc&limit=10&apiKey={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed."}
    