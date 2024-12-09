import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN, API_KEY
import random
from googletrans import Translator
from gtts import gTTS
import os
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())

@dp.callback_query(F.data == 'option_1')
async def option_yes(callback: CallbackQuery):
    await callback.answer("Да")
    await callback.message.edit_text("Вы выбрали: Да")

@dp.callback_query(F.data == 'option_2')
async def option_yes(callback: CallbackQuery):
    await callback.answer("Нет")
    await callback.message.edit_text("Вы выбрали: Нет")

@dp.message(F.text == "Привет!")
async def test_button1(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока!")
async def test_button2(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)


@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('audio.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('doctext.txt')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("training.ogg")
   audi = FSInputFile('training.ogg')
   await bot.send_audio(message.chat.id, audi)
   os.remove("training.ogg")


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

@dp.message(Command('help'))
async def helps(message: Message):
    await message.answer("Я умею выполнять команды:\n/start\n/help\n/photo\n/voice\n/video\n/training\n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.main)

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer( 'Привет', reply_markup=kb.inline_keyboard_test)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer( 'Привет', reply_markup=kb.inline_keyboard)

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

@dp.message(F.text)
async def translate_message(message: Message):
    translated = translator.translate(message.text, dest='en')
    await message.answer(translated.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
