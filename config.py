#   Configuration file

CFG = {
    # Twitch username
    'username' : 'your_username',
    # This is an OAuth token, you can create one at http://www.twitchapps.com/tmi/
    # it must be in the form 'oauth:asd123'
    'password' : 'oauth:your_token',
    # Channel to join on connect, you can leave this the same as your twitch username.
    # If you leave this variable empty, the bot will not join any channel
    'channel'  : 'channel_name',
    # Rate at which the bot works (checks for new messages 1/rate times per second)
    'rate'     : 0.2
}
