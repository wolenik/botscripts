#!/usr/bin/python3
import asyncio
import socket
import netifaces
from telegram import Bot


# Function to get the local IP address
def get_local_ip_address():
    try:
        # Get the IP address associated with the default interface
        ip_address = netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_INET][0]['addr']
        return ip_address
    except Exception as e:
        print(f"Error getting IP address: {str(e)}")
        return None

# Function to send a message to your Telegram bot
async def send_telegram_message(token, chat_id, message):
    try:
        # Initialize the Bot object with your bot's token
        bot = Bot(token=token)
        # Send the message to the chat
        await bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main code
async def main():
    # Telegram bot token
    bot_token = "your telegram bot token"
    # Chat ID of your Telegram bot
    chat_id = "self explanatory"

    # Get the IP address of the Raspberry Pi
    ip_address = get_local_ip_address()

    if ip_address:
        # Construct the message
        message = f"Your Raspberry Pi has connected to the Wi-Fi network. IP address: {ip_address}"
        # Send message to the Telegram bot
        await send_telegram_message(bot_token, chat_id, message)
    else:
        print("Unable to retrieve IP address")

if __name__ == "__main__":
    # Run the asynchronous function within an event loop
    asyncio.run(main())
