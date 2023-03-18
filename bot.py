from aiogram import Bot, Dispatcher, executor, types
from pars import *

bot = Bot(token="6137561129:AAEKUYY9wvxF7_Vtvgk3QqXWeuCDQLE1xG8")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("😷 Covid-19")
    button_2 = types.KeyboardButton('🎮 Games_info')
    button_3 = types.KeyboardButton('🤔 Информация о боте')
    keyboard.add(button_1, button_2).row(button_3)

    await message.answer("Привет, что тебе нужно", reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def func(message):
    if message.text == '🤔 Информация о боте':
        await message.answer("Бот сделан с использованием aiogram, covid-api, cheapshark-api")
    if message.text == '😷 Covid-19':
        await message.answer(covid_api())
    if message.text == '🎮 Games_info':
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)