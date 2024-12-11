import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
from config import TOKEN, NASA_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('space'))
async def space(message: Message):
    url = f'https://api.spacexdata.com/v3/rockets/falcon9'
    response = requests.get(url)

    if response.status_code == 200:
       falcon9 = response.json()
       rocket_name = falcon9['rocket_name']
       first_flight = falcon9["first_flight"]
       await message.answer(f'Тип ракеты {rocket_name},первый полет {first_flight}')
    else:
       await message.answer('Не удалось получить данные.')

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
