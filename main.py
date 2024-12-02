import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.foto)
async def start(message: Message):
    await message.answer('Классная фотка!')

@dp.message(F.text =='Кто ты?')
async def start(message: Message):
    await message.answer('Я искусственный интеллект.')

@dp.message(Command('help'))
async def start(message: Message):
    await message.answer("Я умею выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
