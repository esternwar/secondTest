import telebot
import os
import time
from telebot import types

about = "Описание блюда"
id = [1,2,3,4]
class items:
	def garnir(message):
		bot = telebot.TeleBot('')
		f = open('images/1.jpg', 'rb')
		bot.send_photo(message.chat.id, f, None)
		keyboard = types.InlineKeyboardMarkup()
		it1 = types.InlineKeyboardButton(text="100 гр - 80 р",callback_data='buyy'+str(id[0]))
		keyboard.add(it1)
		bot.send_message(message.chat.id, about, reply_markup=keyboard)
		f = open('images/2.jpg', 'rb')
		bot.send_photo(message.chat.id, f, None)
		keyboard = types.InlineKeyboardMarkup()
		it2 = types.InlineKeyboardButton(text="100 гр - 100 р",callback_data='buyy'+str(id[1]))
		keyboard.add(it2)
		bot.send_message(message.chat.id, about, reply_markup=keyboard)
		f = open('images/3.jpg', 'rb')
		bot.send_photo(message.chat.id, f, None)
		keyboard = types.InlineKeyboardMarkup()
		it3 = types.InlineKeyboardButton(text="100 гр - 75 р",callback_data='buyy'+str(id[2]))
		keyboard.add(it3)
		bot.send_message(message.chat.id, about, reply_markup=keyboard)
		f = open('images/4.jpg', 'rb')
		bot.send_photo(message.chat.id, f, None)
		keyboard = types.InlineKeyboardMarkup()
		it4 = types.InlineKeyboardButton(text="100 гр - 83 р",callback_data='buyy'+str(id[3]))
		keyboard.add(it4)
		bot.send_message(message.chat.id, about, reply_markup=keyboard)		
