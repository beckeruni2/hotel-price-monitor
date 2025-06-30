import json
from utils.scraper import simple_get
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("EMAIL_API_PASSWORD")


def format_email_body(response):
    # Parse the JSON response
    data = json.loads(response)
    check_in = data['result']['chk_in']
    check_out = data['result']['chk_out']
    currency = data['result']['currency']
    rates = data['result']['rates']

    # Build the email body
    body = f"Hotel Rates from {check_in} to {check_out} ({currency}):\n\n"
    for rate in rates:
        platform = rate['name']
        price = rate['rate']
        body += f"{platform}: {price} {currency}\n"
    return body

if __name__ == "__main__":
    # Email details
    sender = email
    receiver = email  # Send to yourself
    password = password  # Your email password or app-specific password


    
    # API URL
    url = 'https://data.xotelo.com/api/rates?hotel_key=g293980-d300674&chk_in=2025-09-14&chk_out=2025-09-19' #queen of Sheba sep14-19

    try:
        # Fetch data from the API
        response = simple_get(url)

        # Format the email body
        email_body = format_email_body(response)

        # Email subject
        subject = "Today's Hotel Rates Update"

        # Create MIMEText object
        msg = MIMEText(email_body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

        print("Email sent!")
    except Exception as e:
        print(f"Error: {e}")




