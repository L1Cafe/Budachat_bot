import requests
import os                                           # For environmental variables
import telegram.ext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = telegram.ext.Updater(token=os.environ["telegramToken"])
dispatcher = updater.dispatcher

# BEGIN DEVELOPMENT FUNCTIONS


def debug(bot, update):
    user = f"ID: {update.message.from_user.id}, Username: @{update.message.from_user.username}, " \
           f"Name: {update.message.from_user.first_name} {update.message.from_user.last_name}, " \
           f"Type: {update.message.from_user.type}"
    bot.send_message(chat_id=update.message.chat_id, text=f"Command called from {update.message.chat.type} ID:"
                                                          f" {update.message.chat_id}"
                                                          f" by {user}")
debug_handler = telegram.ext.CommandHandler("debug", debug)
dispatcher.add_handler(debug_handler)


def test(bot, update):
    entities = ""
    for entity in update.message.entities:
        entities += str(entity)
    entities += update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=f"test {entities}")
    bot.send_message(chat_id=update.message.chat_id, text=f"Collected information:"
                                                          f"SenderUsername: {update.message.from_user.username} - "
                                                          f"SenderFirstName: {update.message.from_user.first_name} - "
                                                          f"SenderID: {update.message.from_user.id}")
    bot.send_message(chat_id=update.message.chat_id, text=f"Hello @{update.message.from_user.username}")
debug_handler = telegram.ext.CommandHandler("test", test)
dispatcher.add_handler(debug_handler)


# END OF DEVELOPMENT FUNCTIONS


def _get_user_name_(user):
    if user.username:
        return f"@{user.username}"
    else:
        return user.first_name


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi!")
start_handler = telegram.ext.CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def start_meditation(bot, update):
    bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id,
                     text=f"{_get_user_name_(update.message.from_user)}"
                     f" started meditating.")
start_meditation_handler = telegram.ext.CommandHandler("start_meditation", start_meditation)
dispatcher.add_handler(start_meditation_handler)


def finish_meditation(bot, update):
    bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id,
                     text=f"{_get_user_name_(update.message.from_user)}"
                     f" finished meditating.")
finish_meditation_handler = telegram.ext.CommandHandler("finish_meditation", finish_meditation)
dispatcher.add_handler(finish_meditation_handler)


updater.start_polling()
