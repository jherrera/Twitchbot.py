# TwitchBotpy

TwitchBotpy is a proof-of-concept bot that connects to Twitch's IRC-like server, written in Python 3.

## Getting started

Open config.py file and type your credentials. The **username** is the user you use to log into Twitch. You will also need an **OAuth token**, which you can make [here](http://www.twitchapps.com/tmi/). Note that I have no connection to this website or its creators. You can also specify a **channel** for the bot to autojoin on connect, or leave it empty to avoid joining any channel.

While the bot is running, you can press `CTRL+C` to set the console in _input mode_, this will allow you to type and send arbitrary IRC commands. You can also type `exit` or `quit` while in _input mode_ to shutdown the bot.