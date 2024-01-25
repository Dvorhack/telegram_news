# Telegram Bot for News events

The Bot opens the port 7878 and sends to telegram everything received on it.

## Usage

Copy `.env.example` to `.env` and fill the variable with your tokens

The Telegram bot can be created using [@BotFather](https://t.me/botfather)

## Add new event

Create a python file in `event_watcher/scripts/` with function `event_watcher()`  
This function will be the base of a thread