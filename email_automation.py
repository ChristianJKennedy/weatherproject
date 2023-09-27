
import os
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
import smtplib

# import weather data
from tempature_object import *

# python plug to read .env files
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"


# load enviorment varibles

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / '.env'
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv('EMAIL')
password_email = os.getenv('PASSWORD')


def send_email(subject, receiver_email, name):
    # create base text
    msg = EmailMessage()
    msg["subject"] = subject
    msg['From'] = formataddr(("Rain jacket today?", f'{sender_email}'))
    msg['To'] = receiver_email
    msg['BCC'] = sender_email

    msg.set_content(
        f'''\
        Hi, {name},
        Here is the weather outlook for today:
        
        City name: {city_name}
        Temperature: {round(fahrenheit_temp)} 
        Humidity: {humidity}
        Wind speed: {wind_speed} 
        Description: {description}
        UV index: {round(uv_index)}
        
    ''')
    # we can add an html version to the email
    # as a second part
    msg.add_alternative(
        f'''\
        <html>
            <body>
                <p>Hi, {name},
                <p>Here is the weather outlook for today:
                <p>
                    City name: {city_name}<br>
                    Temperature: {round(fahrenheit_temp)} F<br>
                    Humidity: {humidity}%<br>
                    Wind speed: {wind_speed} m/s<br>
                    Description: {description}<br>
                    UV index: {round(uv_index)}
                </p>
            </body>
        </html>
        ''',
        subtype='html',
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:

        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Test
if __name__ == "__main__":
    send_email(subject='Arcteryx shell today?',
               receiver_email="test_user@optout.com",
               name='John Smith')






