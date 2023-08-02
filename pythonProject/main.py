import telebot
from telebot import types

bot = telebot.TeleBot("Ваш ключ")

print('_____ START BOT _____')

def simple_numbers(star_value, end_value):
    simple_num = []
    for i in range(star_value, end_value):
        flag = True
        for dil in range(star_value, end_value):
            if dil != 1 and dil < i:
                result = i % dil
                if result == 0:
                    flag = False
                    break
            if dil >= i:
                break
        if flag:
            simple_num.append(i)
    return simple_num

def main_reply_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('⚡Btn 1'), types.KeyboardButton('💧Btn 2'), types.KeyboardButton('🔥Btn 3'))
    markup.row(types.KeyboardButton('Прості числа'))
    markup.row(types.KeyboardButton('Курс Валют'))
    markup.row(types.KeyboardButton('/start'), types.KeyboardButton('/update'))
    return markup

def second_reply_menu():
    markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_2.row(types.KeyboardButton('Долар💷'), types.KeyboardButton('Євро💶'), types.KeyboardButton('Фунт Стерлінга💵'))
    markup_2.row(types.KeyboardButton('/return'))
    return markup_2

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    cid = msg.chat.id
    bot.send_message(cid, "Hello!", reply_markup=main_reply_menu())
	# bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['update'])
def some_msg(msg):
    bot.reply_to(msg, "Update✅", reply_markup=main_reply_menu())

@bot.message_handler(commands=['return'])
def some_msg(msg):
    bot.reply_to(msg, "Returned✅", reply_markup=main_reply_menu())

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	# bot.reply_to(message, message.text)
    cid = msg.chat.id
    if msg.text == 'Прості числа':
        numbers = simple_numbers(1, 100)
        temp_text = 'Список простих чисел: \n\n'
        for num in numbers:
            temp_text += f"{num} "
        bot.send_message(cid, temp_text)
    elif msg.text == 'Курс Валют':
        bot.send_message(cid, 'Оберіть валюту', reply_markup=second_reply_menu())
    elif msg.text == 'Долар💷':
        bot.send_message(cid, 'Курс Доллара:\n1 Доллар - 36,92 Грн.')
    elif msg.text == 'Євро💶':
        bot.send_message(cid, 'Курс Євро\n1 Євро - 40,53 Грн.')
    elif msg.text == 'Фунт Стерлінга💵':
        bot.send_message(cid, 'Курс Фунта Ст.\n1 Фунт - 47,18 Грн.')
bot.infinity_polling()