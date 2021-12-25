"""MODULES"""
import os
import random
import telebot
from dotenv import load_dotenv

load_dotenv()
mToken = os.getenv("BOT_TOKEN")
MEME_SIZE = 17
VER = "v3.0.2"
bot = telebot.TeleBot(mToken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Method"""
    bot.reply_to(message, "Привет, чтобы получить мем от бота наипши: 'Хочу мем'")

@bot.message_handler(commands=['help'])
def send_help(message):
    """Method"""
    bot.reply_to(message, "Просто возьми и напиши 'Хочу мем'")

@bot.message_handler(commands=['version'])
def send_version(message):
    """Method"""
    bot.reply_to(message, VER)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    """Method"""
    if message.text == "Хочу мем":

        # Добавить разнообразных фразочек
        bot.reply_to(message, "Выбираю мем для тебя....")
        mem_id = random.randint(1, MEME_SIZE)
        with open('img/meme'+str(mem_id)+'.jpeg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif random.randint(1, 20) == 10:
        bot.reply_to(message, "Just what do you think you’re doing, Dave?")
    else:
        bot.reply_to(message, "Не понимаю тебя, напиши: 'Хочу мем'")

bot.infinity_polling()
