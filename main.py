import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.photo)
async def answ_photo(message: Message):
    spis = ['Ого, какая фотка!', 'Что это такое?', 'Не отправляй мне такое больше']
    rand_answ = random.choice(spis)
    await message.answer(rand_answ)

@dp.message(F.text =='Кто ты?')
async def answ_mes(message: Message):
    await message.answer('Я искусственный интеллект.')

@dp.message(Command('help'))
async def helps(message: Message):
    await message.answer("Я умею выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
