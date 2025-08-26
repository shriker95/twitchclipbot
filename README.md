# Twitch-Clips-Bot

Posts newly created clips from a Twitch Account to an Discord Channel for your community server e.g.

# Setup


* The get the broadcaster ID from the [TwitchAPI](https://dev.twitch.tv/docs/api/reference/#get-users) with the Username you want the ID from.

* [Register an App on Twitch](https://dev.twitch.tv/docs/authentication/register-app/)

* Create an [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

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

# example crontab

```
*/15 * * * * cd /opt/twitchbot && /opt/twitchbot/bin/python /opt/twitchbot/main.py
```
