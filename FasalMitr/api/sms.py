from twilio.rest import Client

def send_sms_alert(to_number, message, account_sid, auth_token, from_number):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    return message.sid