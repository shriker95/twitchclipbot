# Twitch-Clips-Bot

Adds Clips from Twitch to your DC Channel

# Setup

* install dependencies: `pip install -f requirements.txt`
* create .env file with:
```
# Twitch API
TWITCH_TOKEN_URL=https://id.twitch.tv/oauth2/token
TWITCH_CLIENT_ID=<clientid>
TWITCH_CLIENT_SECRET=<clientsecret>
TWITCH_BROADCAST_ID=<bradcasterid>

# Discord API
DISCORD_WEBHOOK_URL=<webhook url>
```
* create empty file `access_token`

# Run

Run in your desired interval, but dont forget to set it in main.py. (default=15min)