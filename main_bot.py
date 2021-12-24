"""MODULES"""
import os
import random
import telebot
from dotenv import load_dotenv
load_dotenv()
mToken = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(mToken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Method"""
    bot.reply_to(message, "Чтобы получить мем от бота наипши: 'Хочу мем'")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    """Method"""
    if message.text == "Хочу мем":
        bot.reply_to(message, "Meme")
    elif random.randint(1, 10) == 10:
        bot.reply_to(message, "Just what do you think you’re doing, Dave?")
    else:
        bot.reply_to(message, "Не понимаю тебя, напиши: 'Хочу мем'")
