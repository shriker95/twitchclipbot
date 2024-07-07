#!/usr/bin/env python3

import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

twitch_token_url = os.getenv('TWITCH_TOKEN_URL')
twitch_client_id = os.getenv('TWITCH_CLIENT_ID')
twitch_client_secret = os.getenv('TWITCH_CLIENT_SECRET')
twitch_broadcast_id = os.getenv('TWITCH_BROADCAST_ID')

discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

# Interval in minutes
interval = 15

def get_twitch_access_token():
    """Get the access token from Twitch."""
    response = requests.post(
        twitch_token_url,
        data={
            'client_id': twitch_client_id,
            'client_secret': twitch_client_secret,
            'grant_type': 'client_credentials'
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )
    print(response.json())
    response.raise_for_status()
    return response.json()['access_token']

def check_twitch_access_token(twitch_access_token):
    """Check if the access token is still valid."""
    response = requests.get(
        'https://id.twitch.tv/oauth2/validate',
        headers={
            'Authorization': f'OAuth {twitch_access_token}'
        }
    )
    response.raise_for_status()
    if response.status_code == 200:
        return True
    return False

def get_twitch_clips(twitch_access_token):
    """Get the clips from Twitch."""
    start = datetime.datetime.now(datetime.timezone.utc).astimezone() - datetime.timedelta(minutes=interval)
    response = requests.get(
        'https://api.twitch.tv/helix/clips',
        headers={
            'Client-ID': twitch_client_id,
            'Authorization': f'Bearer {twitch_access_token}'
        },
        params={
            'broadcaster_id': twitch_broadcast_id,
            'started_at': start.isoformat(),
            'ended_at': datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
        }
    )
    response.raise_for_status()
    return response.json()

def send_discord_webhook(clip):
    """Send a Discord webhook."""
    response = requests.post(
        discord_webhook_url,
        json={
            'username': 'Twitch Clip Bot',
            'content': f'New clip: {clip["url"]}'
        }
    )
    response.raise_for_status()
    return response

def main():
    with open("access_token", "r") as f:
        token = f.readlines()
        if token.__len__() == 0:
            print('No token found, getting new token...')
            twitch_access_token = get_twitch_access_token()
        else:
            if check_twitch_access_token(token[0]):
                print('Token is still valid.')
                twitch_access_token = token[0]
            else:
                print('Token is invalid, getting new token...')
                twitch_access_token = get_twitch_access_token()
    with open("access_token", "w") as f:
        print('Writing new token to file...')
        f.write(twitch_access_token)
    print('Getting clips...')
    clips = get_twitch_clips(twitch_access_token)
    print('Sending webhooks...')
    for clip in clips['data']:
        print(f'Clip: {clip["url"]}')
        send_discord_webhook(clip)
    

if __name__ == '__main__':
    print('Starting...')
    main()