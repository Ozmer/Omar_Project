import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_sms(text,to):
    message = client.messages \
        .create(
            body=text,
            from_='+15017122661',
            to=to
        )

    print(message.sid)
