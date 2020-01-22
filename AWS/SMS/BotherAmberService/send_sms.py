import os
from twilio.rest import Client
import boto3


TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')

    # account_sid = 'AC25b9b5809efb31d2dd8b0f75a7a5304f'
    # auth_token = '7331487d0b83eb937280179b64322b61'
    account_sid = ssm_client.get_parameter(Name=TWILIO_ACCOUNT_SID, WithDecryption=True)["Parameter"]["Value"]
    auth_token = ssm_client.get_parameter(Name=TWILIO_AUTH_TOKEN, WithDecryption=True)["Parameter"]["Value"]

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(body="Hey babe :) just a friendly reminder for you to get up off your ass and do your homework :P", from_='+14702796969', to='+12707482183')
        print(message.sid)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    lambda_handler(None, None)