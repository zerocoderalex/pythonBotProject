import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, API_KEY
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)


@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('audio.ogg')
    await bot.send_audio(message.chat.id, audio)



@dp.message(Command('photo'))
async def photo(message: Message):
    slist = ['https://cdn.creazilla.com/cliparts/1684366/cloud-with-rain-clipart-sm.png', 'https://cdn.creazilla.com/cliparts/7769144/sun-clouds-rainbow-clipart-md.png']
    rand_photo=random.choice(slist)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')
    

@dp.message(F.photo)
async def react_photo(message: Message):
    spis = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(spis)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(F.text =='Кто ты?')
async def answ_mes(message: Message):
    await message.answer('Я искусственный интеллект.')

@dp.message(Command('help'))
async def helps(message: Message):
    await message.answer("Я умею выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, бот  {message.from_user.first_name}!')

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

@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
