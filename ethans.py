import smtplib
import socket
from email.mime.text import MIMEText
from subprocess import check_output
import time

def get_ip_address():
    ip = check_output(['hostname', '-I']).decode('utf-8')
    return ip.strip()

def send_email(ip_address):
    sender_email = "your_emaiL@email.com"
    receiver_email = "their_email.email.com"
    app_password = "your_app_password"

    message = MIMEText(f"Hello!\n\nYour Raspberry Pi Zero 2 Wireless is connected to the WiFi.\n\nIP Address: {ip_address}")
    message["Subject"] = "Raspberry Pi Connected to WiFi"
    message["From"] = sender_email
    message["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

def main():
    while True:
        try:
            ip_address = get_ip_address()
            send_email(ip_address)
            break
        except Exception as e:
            print("An error occurred:", e)
            time.sleep(10)

if __name__ == "__main__":
    main()
