import telebot
from dotenv import load_dotenv
import os

load_dotenv()

# TODO: Удалить токен demo
mToken = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(mToken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Just what do you think you’re doing, Dave?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()