import asyncio
from telegram import Bot
import socket

# Your Telegram Bot API token
token = '7034943373:AAGKk42G83-JrLVvUr-ymLO20sBVltSB9pI'
bot = Bot(token=token)

# Function to get the device's internal IP address
def get_internal_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        internal_ip = s.getsockname()[0]
        s.close()
        return internal_ip
    except Exception as e:
        print("Error retrieving internal IP address:", e)
        return None

# Function to send a message using Telegram bot
async def send_notification(ip_address, chat_id):
    message = f"Your Raspberry Pi with internal IP address {ip_address} has connected to the network."
    await bot.send_message(chat_id=chat_id, text=message)

    print("Notification sent successfully!")

# Main function
async def main():
    try:
        ip_address = get_internal_ip()
        chat_id = '6885586738'  # Your chat ID or channel ID
        await send_notification(ip_address, chat_id)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

