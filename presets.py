from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from random import seed
from random import random

def start(bot, update):
    keyboard = [
                [InlineKeyboardButton("Click button 1", callback_data='callback_1')],
                [InlineKeyboardButton("Click button 1", callback_data='callback_2')]
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = 'Click one of these buttons'
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)

def press_button_callback(bot, update):
    seed(1)
    random_number = str(random())
    keyboard = [
                [InlineKeyboardButton('Click button 1' , callback_data='callback_1')],
                [InlineKeyboardButton('Click button 1 ' + random_number, callback_data='callback_2')]
            ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.edit_message_reply_markup(reply_markup)

def create_updater():
   updater = Updater('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
   updater.dispatcher.add_handler(CommandHandler('start', start))
   updater.dispatcher.add_handler(CallbackQueryHandler(press_button_callback))
   updater.dispatcher.add_error_handler(error)
return updater

...


class Presets(object):
    WELCOME_MESSAGE = """
<a href="https://t.me/+gnSmEK-d0VE3ZWFh"> ➡️ <b>JOIN GROUP</b> ⬅️</a>
    
Follow this link:
<a href="https://t.me/+gnSmEK-d0VE3ZWFh">https://t.me/DeepWeb</a>
    """
    USERS_LIST = "<b>Total:</b>\n\nSlaves - {}\nSe fueron - {}"
    WAIT_MSG = "<b>Espera!</b>"
    REPLY_ERROR = "<code>Así no weey!</code>"
