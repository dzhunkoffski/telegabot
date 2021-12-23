"""MODULES"""
import os
import telebot
from dotenv import load_dotenv

load_dotenv()

mToken = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(mToken)

# Some dummy change to test CD

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Method"""
    bot.reply_to(message, "Just what do you think you’re doing, Dave?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    """Method"""
    bot.reply_to(message, "Test")


bot.infinity_polling()