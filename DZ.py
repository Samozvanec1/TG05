import asyncio # отвечаут за асинхронность
from aiogram import Bot, Dispatcher # библиотека для бота
from aiogram.filters import CommandStart, Command # фильтры для бота
from aiogram.types import Message # типы для бота
import requests # библиотека для запросов
import time #
from random import randint

from config import TOKEN

import logging # для логирования

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Напиши статус-код или введи команду /randog, и я пришлю тебе картинку.")

@dp.message(Command("randog"))
async def random_dog(message: Message):
    Geting = True
    while Geting == True:
        code = randint(200, 527)
        api = f"https://http.dog/{code}.jpg"
        if requests.get(api).status_code == 200:
            Geting = False
    api = f"https://http.dog/{code}.jpg"
    await message.answer_photo(api)

@dp.message()
async def responce_dogs(message: Message): # функция для бота
    try:
        code = message.text # код для бота
        api = f"https://http.dog/{code}.jpg"
        await message.answer_photo(api)
    except Exception as ex:
        await message.answer("Вводить с 200 по 527")
        print(ex)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())