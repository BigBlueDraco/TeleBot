import os
import random
import telebot


API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('1861696662:AAHNDz8cOqa0AvIyRFRuw_9DJK_vXBukqlM')


@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Привет я могу ролить дайсы за тебя")


@bot.message_handler(['roll'])
def roll(message):
    bot.send_message(message.chat.id, 'ДАвай ролить \n Для  напиши какую  кость ролить ')


@bot.message_handler(['d2'])
def roll_d2(message):
    a = random.randint(1, 2)
    bot.reply_to(message, a)


bot.polling(none_stop=True)
