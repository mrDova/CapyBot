import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6301767993:AAHSZZhEXTQz3hVc_ymyO_OLxPVkpVbkU3w')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Привет, CapyBot☀️')
    markup.row(btn1)
    bot.send_message(message.chat.id, f'Привет капибобрик, {message.from_user.first_name}!👋', reply_markup=markup)
    bot.register_next_step_handler(message, nachalo)

def nachalo(message):
    if message.text == 'Привет, CapyBot☀️':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Мой Курс❤️')
        btn2 = types.KeyboardButton('Беседа Летнего Курса ОГЭ')
        btn3 = types.KeyboardButton('Телеграм-канал Капибары')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)




def vcurs(message):
    if message.text == 'Мой Курс❤️':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Занятие 1 «Введение Анатомию» (22.07.23)')
        btn2 = types.KeyboardButton('Занятие 2 «Остеология.Миология.Синдесмология» (24.07.23)')
        btn3 = types.KeyboardButton('Занятие 3 «Спланхнология» (26.07.23)')
        btn4 = types.KeyboardButton('Занятие 4 «Кровеносная и Дыхательная системы» (29.07.23)')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id, '✨Вот занятия  Летнего Курса ЕГЭ по цитологии, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == 'Беседа Летнего Курса ОГЭ':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    elif message.text == 'Телеграм-канал Капибары':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на Телеграм-канал', url='https://t.me/capybara_school')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это наш основной канал, тут преподаватель делится многими интересными и полезными материалами , а так же рассказывает о своей жизни, медицине и биологии.', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, vcurs)




def zad(message):
    if message.text == 'Занятие 1 «Введение Анатомию» (22.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Скрипт', url='https://monkeytype.com')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, 'https://youtu.be/_1V37GKlOHE', reply_markup=markup)
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 2 «Остеология.Миология.Синдесмология» (24.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Скрипт', url='https://monkeytype.com')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, 'https://youtu.be/_1V37GKlOHE', reply_markup=markup)
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 3 «Спланхнология» (26.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Скрипт', url='https://monkeytype.com')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, 'https://youtu.be/_1V37GKlOHE', reply_markup=markup)
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 4 «Кровеносная и Дыхательная системы» (29.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Скрипт', url='https://monkeytype.com')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, 'https://youtu.be/_1V37GKlOHE', reply_markup=markup)
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, zad)

def hlp(message):
    if message.text == 'Курс 1' or message.text == 'Выбрать другое занятие':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Занятие 1 «Введение Анатомию» (22.07.23)')
        btn2 = types.KeyboardButton('Занятие 2 «Остеология.Миология.Синдесмология» (24.07.23)')
        btn3 = types.KeyboardButton('Занятие 3 «Спланхнология» (26.07.23)')
        btn4 = types.KeyboardButton('Занятие 4 «Кровеносная и Дыхательная системы» (29.07.23)')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id, '✨Вот занятия  Летнего Курса ЕГЭ по цитологии, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, hlp)




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'dz1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, 'Вот ссылка на твоё домашнее задание: https://t.me/baisov_islam', reply_markup=markup)
    if callback.data == 'dz2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, 'Вот ссылка на твоё домашнее задание: https://t.me/baisov_islam', reply_markup=markup)
    if callback.data == 'dz3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, 'Вот ссылка на твоё домашнее задание: https://t.me/baisov_islam', reply_markup=markup)


@bot.message_handler(commands=['restart'])
def restart(message):
    bot.register_next_step_handler(message, start)

@bot.message_handler(commands=['info'])
def main(message):
    bot.delete_my_commands()
    bot.clear_step_handler()
    bot.send_message(message.chat.id, message)


bot.infinity_polling()
