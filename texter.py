from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_PHONE
from twilio.rest import Client
import json

from analyze import analyze_data
from quant import gen_suggestion

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_update(user_id):
    """Texts the user analyzed stock data based on their listed stocks"""
    with open("users.json", "r") as file:
        data = json.load(file)

    user_info = data.get(user_id)

    message = client.messages.create(
        body = analyze_data(user_id) + gen_suggestion(user_id),
        from_ = FROM_PHONE,
        to = user_info.get('phone')
    )
    print(f"Message SID: {message.sid}")