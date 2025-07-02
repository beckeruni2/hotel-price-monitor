import json
import math
from utils.scraper import simple_get
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("EMAIL_API_PASSWORD")
password2 = os.getenv("EXCHANGE_RATE_API_PASSWORD")


def format_email_body(response):
    check_in = response['result']['chk_in']
    check_out = response['result']['chk_out']
    currency = response['result']['currency']
    rates = response['result']['rates']

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
    url2 = 'https://v6.exchangerate-api.com/v6/' + password2 + '/latest/USD'  # Exchange rate API URL



    try:
        response = simple_get(url)  # Fetch the hotel rates
        response2 = simple_get(url2)  # Fetch the current exchange rates

        rate = response2['conversion_rates']['ILS']  # Access the conversion rate for ILS
        response['result']['currency'] = 'ILS'  # Set the currency to ILS

        for r in response['result']['rates']:
            r['rate'] = math.floor(r['rate']*rate)  # Convert the rate to ILS using the exchange rate

        # Format the email body
        email_body = format_email_body(response)

        # Email subject
        subject = "Today's Hotel Rates Update"

        # Create MIMEText object
        msg = MIMEText(email_body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver
        
        #Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

            print(response)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")




