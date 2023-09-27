from datetime import date
from email_automation import *


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


result = query_data_and_send_emails(df)
print(result)