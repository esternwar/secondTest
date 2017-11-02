from telebot import types
import telebot
from unit import items
import os
from flask import Flask, request

bot = telebot.TeleBot('432228990:AAFI4tjOzj-0esXcO-afVe-oA004EZPEDow')

@bot.message_handler(commands=['start'])	
def custom(message):
	markup = types.ReplyKeyboardMarkup()
	markup.row('\U0001F374 Меню', '\U0001F4E6 Корзина')
	markup.row('\U0001F4E6 Заказы', '\U0001F4E2 Новости')
	bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)
	#return markup
	
	
def home(message):
	markup = types.ReplyKeyboardMarkup()
	markup.row('\U0001F3E0 Домой')
	bot.send_message(message.chat.id, "Выбранна:", reply_markup=markup)
	return markup


	
@bot.message_handler(regexp="\U0001F3E0 Домой")
def homy(message):
        custom(message)
        
@bot.message_handler(regexp="\U0001F374 Меню")
def default_test(message):
    home(message)
    keyboard = types.InlineKeyboardMarkup()
    urop = types.InlineKeyboardButton(text="Европейское меню",callback_data='urop')
    asia = types.InlineKeyboardButton(text="Японское меню",callback_data='asia')
    pizza = types.InlineKeyboardButton(text="Пицца",callback_data='pizza')
    keyboard.add(urop,asia)
    keyboard.add(pizza)
    bot.send_message(message.chat.id, "Меню\n\nВыбери кухню", reply_markup=keyboard)

@bot.message_handler(regexp="\U0001F4E6 Корзина")
def buy(message):
    home(message)
    keyboard = types.InlineKeyboardMarkup()
    urop = types.InlineKeyboardButton(text="Корзина",url='https://ya.ru')
    keyboard.add(urop)
    bot.send_message(message.chat.id, "Купить", reply_markup=keyboard)

@bot.message_handler(regexp="\U0001F4E6 Заказы")
def story(message):
    home(message)
    keyboard = types.InlineKeyboardMarkup()
    urop = types.InlineKeyboardButton(text="Обложка",callback_data='urop')
    keyboard.add(urop)
    bot.send_message(message.chat.id, "Мои покупки", reply_markup=keyboard)

@bot.message_handler(regexp="\U0001F4E2 Новости")
def news(message):
    home(message)
    keyboard = types.InlineKeyboardMarkup()
    urop = types.InlineKeyboardButton(text="Новости",callback_data='urop')
    keyboard.add(urop)
    bot.send_message(message.chat.id, "Новости", reply_markup=keyboard)
    



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "urop":
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=uro(call.message.chat.id))
        if call.data == "asia":
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=asi(call.message.chat.id))
        if call.data == "pizza":
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=asi(call.message.chat.id))
        if call.data == "default_test":
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            default_test(call.message)
        if call.data == "garn":
            items.garnir(call.message)
        if call.data == "a":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='БЛЮДА')

def uro(msg):
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Гарнир",callback_data='garn')
    item2 = types.InlineKeyboardButton(text="Рыба",callback_data='a')
    item3 = types.InlineKeyboardButton(text="Супы",callback_data='a')
    item4 = types.InlineKeyboardButton(text="Второе блюдо",callback_data='a')
    item5 = types.InlineKeyboardButton(text="Назад",callback_data='default_test')
    keyboard.add(item1,item2)
    keyboard.add(item3,item4)
    keyboard.add(item5)
    return keyboard

def asi(msg):
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Суши",callback_data='a')
    item2 = types.InlineKeyboardButton(text="Роллы",callback_data='a')
    item3 = types.InlineKeyboardButton(text="Темпура",callback_data='a')
    item4 = types.InlineKeyboardButton(text="Рамен",callback_data='a')
    item5 = types.InlineKeyboardButton(text="Назад",callback_data='default_test')
    keyboard.add(item1,item2)
    keyboard.add(item3,item4)
    keyboard.add(item5)
    return keyboard
	
def piz(msg):
    keyboard = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text="Обычная",callback_data='a')
    item2 = types.InlineKeyboardButton(text="Студенческая",callback_data='a')
    item3 = types.InlineKeyboardButton(text="Просроченная",callback_data='a')
    item4 = types.InlineKeyboardButton(text="Заебался писать",callback_data='a')
    item5 = types.InlineKeyboardButton(text="Назад",callback_data='default_test')
    keyboard.add(item1,item2)
    keyboard.add(item3,item4)
    keyboard.add(item5)
    return keyboard

server = Flask(__name__)


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://botniceref.herokuapp.com/")
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
