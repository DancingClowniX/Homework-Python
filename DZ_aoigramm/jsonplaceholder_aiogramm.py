import aiogram
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
from aiogram.filters import Command, CommandObject
from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
import requests

TOKEN = "ВАШ ТОКЕН"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Вы в боте по работе с api jsonplaceholder,Привет {html.bold(message.from_user.full_name)}')
@dp.message(Command('users'))
async def command_users_handlermessage(message: Message)-> None:
    if message:
        url = 'https://jsonplaceholder.typicode.com/users'
        json_data = requests.get(f'{url}').json()
        listName = []
        for name in json_data:
            listName.append(name['name'])
        await message.answer(f"Привет! Список пользователей: {listName}")
    else:
        await message.answer("сообщения не было.")

@dp.message(Command(f'user'))
async def command_user_handler(message: Message, command: CommandObject) -> None:
    command_args: str = command.args
    if command_args:
        command_args = int(command_args)
        if command_args > 10:
            await message.answer("В списке только 10 человек.")
        else:
            url = 'https://jsonplaceholder.typicode.com/users'
            json_data = requests.get(f'{url}').json()
            for item in json_data:
                for id in item:
                    if item[id] == command_args:
                        await message.answer(f"""
Имя: {item['name']}\nНик: {item['username']}
email: {item['email']}
адрес: улица {item['address']['street']}
        дом/кв {item['address']['suite']}
        город {item['address']['city']}    
        почтовый индекс {item['address']['zipcode']}
        локация: ширина {item['address']['geo']['lat']}
                долгота {item['address']['geo']['lng']}
Тел: {item['phone']}
Сайт: {item['website']}
""")
                        break
                    else:
                        break
    else:
        await message.answer("Привет! Ты не указал id пользователя.")

@dp.message(Command('posts'))
async def command_posts_handlermessage(message: Message)-> None:
    if message:
        url = 'https://jsonplaceholder.typicode.com/posts'
        json_data = requests.get(f'{url}').json()
        listPosts = []
        for all_posts in json_data:
            del all_posts['id']
            del all_posts['userId']
            del all_posts['body']
            listPosts.append(all_posts)
            if len(listPosts)==10:
                break
            else:
                continue
        await message.answer(f"Список 10 первых постов:{listPosts}")
    else:
        await message.answer("сообщения не было.")

@dp.message(Command('userpost'))
async def command_user_handler(message: Message, command: CommandObject) -> None:
    command_args: str = command.args
    if command_args:
        command_args = int(command_args)
        if command_args > 10:
            await message.answer("В списке только 10 человек.")
        else:
            url = f'https://jsonplaceholder.typicode.com/posts?userId={command_args}'
            json_data = requests.get(f'{url}').json()
            url2 = f'https://jsonplaceholder.typicode.com/users?id={command_args}'
            obj_user = requests.get(f'{url2}').json()
            user = obj_user[0]['name']
            listPosts = []
            for title in json_data:
                del title['id']
                del title['userId']
                del title['body']
                listPosts.append(title['title'])
            await  message.answer(f'Список постов {listPosts}, Пользователя <b>{user}</b>')



bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
