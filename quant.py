import json

from analyze import convert_date
from datetime import datetime, timedelta
from fetch import fetch_ma
# # # Suggests to the user a stock to buy or sell out of their securities

def calc_ma(stock, window):
    """Calculate short term moving average for a particular stock (last 10 days)"""
    return fetch_ma(stock, window)['results']['values'][0]['value']

# TODO IN FUTURE: Keep state of sma/lma relations for each stock....
# When they shift, trigger the lambda to signal buy/sell
def decide(stock, sma, lma):
    # Buy signal
    if sma > lma:
        return "Buy"
    # Sell signal
    elif lma < sma:
        return "Sell"
    else:
        return "Hold"

def gen_suggestion(user_id):
    str = "\n\n"

    with open("users.json", "r") as file:
        data = json.load(file)

    if user_id in data:
        str = f"\n Suggested move:\n \n"
        max = 0
        stock = ""
        long_window = 50
        short_window = 10
        max_sma = 0
        max_lma = 0

        for curr_stock in data[user_id]['stocks']:        
            
            sma = calc_ma(curr_stock, short_window)
            sma = round(sma, 2)

            lma = calc_ma(curr_stock, long_window)
            lma = round(lma, 2)                     
            current = abs(sma - lma)
            # Calculating the largest difference in sma and lma
            if current > max:
                max = current
                max_sma = sma
                max_lma = lma
                stock = curr_stock

        max = round(max, 2)
        str += f"{decide(stock, max_sma, max_lma)} {stock}!"
                        
    else:
        return {"error": "User is not defined."}

    return str
