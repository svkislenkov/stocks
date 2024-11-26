from datetime import datetime, timedelta
from fetch import fetch_data
import json

def convert_date(date):
    """Convert Saturday/Sunday to previous Friday """
    if date.weekday() == 5:  # Sat
        return date - timedelta(days=1)
    elif date.weekday() == 6:  # Sun
        return date - timedelta(days=2)
    return date

def weekly_average(stock, today):
    """Find weekly average for stock's weighted daily volume"""
    sum = 0
    for i in range(1, 8):
        date = convert_date(today - timedelta(days=i))
        data = fetch_data(stock, date.date().strftime("%Y-%m-%d"))
        # print(data)
        sum += data['results'][0]['vw']
    return sum / 7

def gen_comparison(stock, price_today, price_week):
    """Return a comparison between two prices"""
    str = f"{stock} (${price_today}) "
    diff = price_today - price_week
    if diff > 0:
        return str + f"is up from a weekly average of ${price_week} 📈\n\n"
    elif diff < 0:
        return str + f"is down from a weekly average of ${price_week} 📉\n\n"
    return str + "is the exact same as last week's average!\n\n"

def analyze_data(user_id):
    """Return a summary of a user's stocks"""
    with open("users.json", "r") as file:
        data = json.load(file)

    today = convert_date(datetime.now())
    
    if user_id in data:
        str = f"\n Weekly summary for {data[user_id]['first_name']} {data[user_id]['last_name']}:\n \n"
        for stock in data[user_id]['stocks']:            
            
            price_week = weekly_average(stock, today)            
            price_today = fetch_data(stock, today.date().strftime("%Y-%m-%d"))['results'][0]['vw']

            price_week = round(price_week, 2)
            price_today = round(price_today, 2)

            summary = gen_comparison(stock, price_today, price_week)

            str += summary
    else:
        return {"error": "User is not defined."}
    
    return str