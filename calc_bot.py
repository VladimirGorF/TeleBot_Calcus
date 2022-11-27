import datetime
import telebot
import Calcus


API_TOKEN = '5936246114:AAGCbe54p6aXYNxWmFa0iaKnh05wosaWSus'


bot = telebot.TeleBot(API_TOKEN)
print('Server started')


@bot.message_handler(commands=['start'])
def help_message(message):
    bot.send_message(message.chat.id,f"/time\n/calcus")


@bot.message_handler(commands=['calcus'])
def help_message(message):
    bot.send_message(message.chat.id,f"Выберите тип вычислений: \n/rational\n/complex")


@bot.message_handler(commands=['time'])
def time_message(message):
    bot.send_message(message.chat.id,f"Текущее время {datetime.datetime.now()}")


@bot.message_handler(commands=['rational'])
def calc_message(message):
    ex = message.text.split()[1:]
    bot.send_message(message.chat.id,f"Введите '/', затем через пробел ведите, что требуется посчитать.")

@bot.message_handler(commands=[''])
def calc_message(message):
    ex = message.text.split()[1:]
    bot.send_message(message.chat.id,f"А  вот и ответ:  {Calcus.Calcus(ex[0])} ")

@bot.message_handler(commands=['complex'])
def calc_message(message):
    ex = message.text.split()[1:]
    bot.send_message(message.chat.id,f"Введите '/cx', затем через пробел введите, что требуется посчитать.")


@bot.message_handler(commands=['cx'])
def calc_message(message):
    ex = message.text.split()[1:]
    bot.send_message(message.chat.id,f"А  вот и ответ:  {eval(ex[0])} ")

@bot.message_handler(content_types='text')
def message_reply(message):
    if 'привет' in message.text:
        bot.send_message(message.chat.id, 'и тебе привет')


bot.polling()
