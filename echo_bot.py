import telebot

# TODO: Удалить токен
bot = telebot.TeleBot("5033258071:AAEzrJiI4HAPhB9XQaYD28AIdTsheanTWLc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Just what do you think you’re doing, Dave?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()