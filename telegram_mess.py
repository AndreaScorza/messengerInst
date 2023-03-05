import requests
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
bot_token = os.getenv('bot_token')
chat_id = os.getenv('chat_id')
    
def send_message(message):
    # Compose the URL for the Telegram Bot API endpoint
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    url = f"{base_url}?chat_id={chat_id}&text={message}"

    # Send the HTTP request to the Telegram Bot API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError("Failed to send message")

    # Parse the response JSON (optional)
    response_json = response.json()

    # Return the response JSON (optional)
    return response_json



