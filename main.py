from datetime import date
import pandas as pd
from email_automation import *

# public google sheet url
SHEET_ID = '10_CZKmK5q0CQjwvGMmm31Cciy3QfnZy-eZAl42MAlqI'
SHEET_NAME = 'Sheet1'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

# Create function for data framework
def load_df(url):
    today_date = ['date', 'notifications_yn']
    df = pd.read_csv(url, parse_dates=today_date)
    return df

# frunction to parse through framework and send emails according to user notification preference
# later on more information can be added to opt in or out of certain weather information
def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present == row['date'].date()) and (row['notifications_yn'] == 'Yes'):
            send_email(
                subject='Arcteryx shell today?',
                receiver_email=row['Email'],
                name=row['Name'])

            email_counter += 1
    return f'Total emails sent: {email_counter}'


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)