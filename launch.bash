#!/bin/bash

# Telegram Bot token
export telegramToken="<YOUR TELEGRAM TOKEN HERE>"
# Telegram admin ID
export telegramAdminId="<YOUR ID HERE>"
# Telegram chat ID
export telegramChatId="<YOUR GROUP ID HERE>"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

`which python3.6` budachat/bot.py
