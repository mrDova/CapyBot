import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6301767993:AAHSZZhEXTQz3hVc_ymyO_OLxPVkpVbkU3w')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Привет, CapyBot☀️')
    markup.row(btn1)
    bot.send_message(message.chat.id, f'Привет капибобрик, {message.from_user.first_name}!👋', reply_markup=markup)
    bot.register_next_step_handler(message, nachalo)

def nachalo(message):
    if message.text == 'Привет, CapyBot☀️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Мой Курс❤️')
        btn2 = types.KeyboardButton('Беседа Летнего Курса ЕГЭ')
        btn3 = types.KeyboardButton('Телеграм-канал Капибары')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, nachalo)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, nachalo)



def vcurs(message):
    if message.text == 'Мой Курс❤️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1 (21.07.23)')
        btn2 = types.KeyboardButton('Занятие 2 (25.07.23)')
        btn3 = types.KeyboardButton('Занятие 3 (28.07.23)')
        btn4 = types.KeyboardButton('Занятие 4 (01.08.23)')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id, '✨Вот занятия  Летнего Курса ЕГЭ по цитологии, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == 'Беседа Летнего Курса ЕГЭ':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
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
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, vcurs)




def zad(message):
    if message.text == 'Занятие 1 (21.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«ВВЕДЕНИЕ В ЦИТОЛОГИЮ»</b> \n <i>Дата онлайн-занятия:21.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/07qXGV0nbVk?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 2 (25.07.23)': 
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp2')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz2')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 2 <b>«КЛЕТОЧНЫЙ ЦИКЛ.МИТОЗ»</b> \n <i>Дата онлайн-занятия:25.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://t.me/c/1848151860/8 ', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 3 (28.07.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp3')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz3')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 3 <b>«МЕЙОЗ.ГАМЕТОГЕНЕЗ»</b> \n <i>Дата онлайн-занятия:28.07.2023</i> \n <i>Время: 10:00 мск</i> \n ( Запись появится после трансляции, а пока распечатай скрипт и насладись видосиком с Капибарами ) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 4 (01.08.23)':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp4')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz4')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 4 <b>«ЦИКЛЫ РАСТЕНИЙ»</b> \n <i>Дата онлайн-занятия:01.08.2023</i> \n <i>Время: 10:00 мск</i> \n ( Запись появится после трансляции, а пока распечатай скрипт и насладись видосиком с Капибарами ) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, zad)

def hlp(message):
    if message.text == 'Выбрать другое занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1 (21.07.23)')
        btn2 = types.KeyboardButton('Занятие 2 (25.07.23)')
        btn3 = types.KeyboardButton('Занятие 3 (28.07.23)')
        btn4 = types.KeyboardButton('Занятие 4 (01.08.23)')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.send_message(message.chat.id, '✨Вот занятия  Летнего Курса ЕГЭ по цитологии, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, hlp)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попоробуем ещё раз')
        bot.register_next_step_handler(message, hlp)




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'dz1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'<a href="https://docs.google.com/forms/d/e/1FAIpQLSf-pKKI_n_VT5ivjrvWy_UetjP2aROYkML-7FecAuSMJvX3bw/viewform?usp=share_link">Вот ссылка на дз к занятию 1</a>', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, '( Дз скоро появится, а пока  насладись видосиком с Капибарами): https://youtu.be/wcov8v0hrHY', reply_markup=markup)
    if callback.data == 'dz3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, '( Дз скоро появится, а пока  насладись видосиком с Капибарами): https://youtu.be/wcov8v0hrHY', reply_markup=markup)
    if callback.data == 'dz4':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, '( Дз скоро появится, а пока  насладись видосиком с Капибарами): https://youtu.be/wcov8v0hrHY ', reply_markup=markup)
    if callback.data == 'skrp1':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/file/d/1awCmoCCKm_lPLCgYOCZ_swop9AhToYl9/view?usp=share_link">Вот ссылка на скрипт к занятию 1</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp2':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/file/d/1oVQvwtF7gOiqsvDP93X_GwfYHOBLxXMy/view?usp=drivesdk">Вот ссылка на скрипт к занятию 2</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp3':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/file/d/1f9-ofS2dkUP-wkVcQ5OeqOYx1xsR2AKa/view?usp=share_link">Вот ссылка на скрипт к занятию 3</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp4':
        bot.send_message(callback.message.chat.id, '( Скрипт скоро появится, а пока  насладись видосиком с Капибарами): https://youtu.be/wcov8v0hrHY ')
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, hlp)


def link(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+modSPJz7XQMyYmQy')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
    bot.register_next_step_handler(message, hlp)

    

@bot.message_handler(commands=['restart'])
def restart(message):
    bot.register_next_step_handler(message, start)

@bot.message_handler(commands=['info'])
def main(message):
    bot.delete_my_commands()
    bot.clear_step_handler()
    bot.send_message(message.chat.id, message)


bot.infinity_polling()
