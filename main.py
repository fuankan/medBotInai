import requests
import json
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from decouple import config

TOKEN = '5755658521:AAFh1CTOBb7VtuzeARSLoXb-BcG9V_UZ270'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}')


@dp.message_handler(commands=['parser'])
async def memes_parser(message: types.Message):
    rsp = requests.get("https://api.imgflip.com/get_memes")
    data = json.JSONDecoder().decode(rsp.text)['data']['memes']

    for meme in data[:10]:
        await bot.send_photo(
            message.chat.id,
            meme['url'],
        )

        await bot.send_message(
            message.chat.id,
            meme['name']
        )

# 1
@dp.message_handler(commands=['games'])
async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая задача",
                                         callback_data='next_task1')
    markup.add(button_call_1)
    question = 'Какая из этих частей человека имеет крылья?'
    answers = ['Нос', 'Спина', 'Губы', 'Люде не летают']
    photo = open('media/fly.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup,
        open_period=30,
        explanation='Это очень легкий вопрос, если не знаешь, то загугли',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


# 2
@dp.callback_query_handler(lambda func: func.data == 'next_task1')
async def games_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = 'Органы какого из этих чувств человека расположены не только в голове?'
    answers = ['Слух', 'Обоняние', 'Осязание', 'Зрение']
    photo = open('media/human.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question2,
        options=answers,
        correct_option_id=2,
        open_period=30,
        explanation='Не скажу',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


# 3
@dp.callback_query_handler(lambda func: func.data == 'next_task2')
async def task_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая задача", callback_data='next_task3')
    markup.add(button_call_3)
    question3 = 'В каком возрасте у ребёнка происходит окостенение коленных чашечек?'
    answers3 = ['10-12 месяцев', '3-6 месяцев', '3-6 лет', '1-2 Года']
    photo = open('media/baby.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question3,
        options=answers3,
        correct_option_id=2,
        open_period=30,
        explanation='Что большего места в организме занимает?',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


# 4
@dp.callback_query_handler(lambda func: func.data == 'next_task3')
async def task_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Следующая задача", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = 'Сколько всего ягодичных мышц в теле человека?'
    answers4 = ['2', '6', '8']
    photo = open('media/anatomy.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answers4,
        correct_option_id=1,
        open_period=30,
        explanation='T_T',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


@dp.callback_query_handler(lambda func: func.data == 'next_task4')
async def task_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task5')
    markup.add(button_call_5)
    question5 = 'Что в человеке продолжает расти всю жизнь?'
    answers5 = ['Рост', 'зубы', 'волосы']
    photo = open('media/hair.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question5,
        options=answers5,
        correct_option_id=2,
        open_period=30,
        explanation='Это еще каждый выпадает',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


@dp.callback_query_handler(lambda func: func.data == 'next_task5')
async def task_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Следующая задача", callback_data='next_task6')
    markup.add(button_call_5)
    question5 = 'Самая сильная мышца в человеческом теле?'
    answers5 = ['Прямая мышца бедра', 'Большая грудная мышца', 'Жевательная мышца']
    photo = open('media/muscle.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question5,
        options=answers5,
        correct_option_id=2,
        open_period=30,
        explanation='Вопрос с подвохом',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
