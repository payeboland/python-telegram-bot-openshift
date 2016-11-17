# Copyright (C) 2016 Javier Ayres
#
# This file is part of python-telegram-bot-openshift.
#
# python-telegram-bot-openshift is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-telegram-bot-openshift is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-telegram-bot-openshift.  If not, see <http://www.gnu.org/licenses/>.

import logging
from queue import Queue
from threading import Thread
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, MessageHandler, Updater, CommandHandler, CallbackQueryHandler, InlineQueryHandler
import maker

TOKEN = '200657939:AAEvM5T3WghxDBZRQ2tM680abBUFmAseUxc'

status="zero"
background="NO"
name="NO"
phone="NO"
desc="NO"

def start(bot, update):	
    keyboard = [[InlineKeyboardButton("ساخت کارت ویزیت", callback_data='start_cmd')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('سلام {} عزیز! به ربات کارت ویزیت ساز خوش آمدید'.format(update.message.from_user.first_name), reply_markup=reply_markup)


def example_handler(bot, update):
    global status
    global name
    global phone
    global desc

    if status[0]=='b':
        status='n'
        nametext = update.message.text
        name=nametext
        bot.send_message(
            update.message.chat_id,
            text="مرحله ی چهارم: شماره ی تلفنی که می خواهید روی کارت درج شود را وارد کنید."
            )  

    elif status=='n':
        status='t'
        phonetext = update.message.text
        phone=phonetext
        bot.send_message(
            update.message.chat_id,
            text="مرحله ی پنجم: توضیحاتی که میخواهید روی کارت درج شود را وارد کنید."
            )  

    elif status=='t':
        status='d'
        desctext = update.message.text
        desc=desctext
        
        res="نام :"+ name + "تلفن :"+ phone + "توضیحات :"+ desc + "بکگراند :"+ background 
        bot.send_message(
            update.message.chat_id,
            text=res
            )  
        
        bot.sendPhoto(chat_id=chat_id, photo=open(maker.maker1(name,phone,desc), 'rb'))

    else :  
        bot.send_message(
            update.message.chat_id,
            text=" را وارد کنید /start برای استفاده از ربات و ساخت کارت ویزیت "
            ) 


def button(bot, update):
    query = update.callback_query
    global status
    global background
    status= query.data

    if status=='start_cmd':
        keyboard = [[InlineKeyboardButton("پس زمینه ی شماره ۱", callback_data='bg1'),InlineKeyboardButton("پس  زمینه ی شماره ۲", callback_data='bg2')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="مرحله ی دوم: انتخاب پس زمینه",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id , reply_markup=reply_markup)
    
    elif status[0]=='b':
        background=status
        bot.editMessageText(text="مرحله ی سوم: لطفا نام مورد نظر خود برای درج روی کارت را بنویسید.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)




# Write your handlers here


def setup(webhook_url=None):
    """If webhook_url is not passed, run with long-polling."""
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:
        updater = Updater(TOKEN)
        bot = updater.bot
        dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler([], example_handler))
    dp.add_handler(CallbackQueryHandler(button))



    if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    setup()
