import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, API_KEY
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo'))
async def photo(message: Message):
    slist = ['https://cdn.creazilla.com/cliparts/1684366/cloud-with-rain-clipart-sm.png', 'https://cdn.creazilla.com/cliparts/7769144/sun-clouds-rainbow-clipart-md.png']
    rand_photo = random.choice(slist)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    spis = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
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


@dp.message(Command('weather'))
async def weather(message: Message):
    # Получение данных о погоде
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Москва&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        await message.answer(f'Температура в Москве: {temp}°C')
    else:
        await message.answer('Не удалось получить данные о погоде.')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
