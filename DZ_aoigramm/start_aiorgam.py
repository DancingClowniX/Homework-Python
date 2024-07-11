import datetime

import aiogram
import asyncio
import logging
import sys

import time
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.filters import Command
from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = "ВАШ ТОКЕН"
dp = Dispatcher()
manager = '@cockieMonsta'
time = datetime.datetime.now()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'hello,{html.bold(message.from_user.full_name)}')

@dp.message(F.text, Command('help'))
async def command_help_handler(message: Message)-> None:
    await message.answer(f'Поддержка бота, реакция на help')

#бесконечный запуск бота
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(Command('photo'))
async def command_photo_handler(message: Message)-> None:
    await message.answer_photo('https://cdn-img.perekrestok.ru/i/800x800-fit/xdelivery/files/da/0f/9b5a9d03a5ebf3240374e3db5a76.jpg')

@dp.message(Command('sticker'))
async def command_sticker_handler(message: Message)-> None:
    await message.answer_sticker('CAACAgIAAxkBAAEMbFtmhYfDTz2nGk6Bqh6IvbBj5WoSOwACJAMAArVx2gafiis85FHPvTUE')

@dp.message(Command('ask'))
async def command_ask_handler(message: Message)-> None:
    await message.answer(f'Для связи обратитесь к,{html.bold(manager)}')

@dp.message(Command('time'))
async def command_time_handler(message: Message)-> None:
    await message.answer(f'{time.hour}:{time.minute}:{time.second}')



geo_btn: KeyboardButton = KeyboardButton(
    text="Заказать геолокацию",
    request_location=True
)

keyboard = ReplyKeyboardMarkup(keyboard=[[geo_btn]], resize_keyboard=True)


@dp.message(Command(commands="button"))
async def cmd_start(message: Message):
    await message.answer(
        text='Клавиатура вот такая',
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
