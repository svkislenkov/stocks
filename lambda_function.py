import json

from texter import send_update

def lambda_handler(event, context):
    """For each specified user, texts them the result"""
    with open("users.json", "r") as file:
        data = json.load(file)
    
    for user_id in data:
        send_update(user_id)

lambda_handler(1, 2)