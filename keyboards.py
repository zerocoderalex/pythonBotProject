from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет!")],
   [KeyboardButton(text="Пока!")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/watch?v=HfaIcB4Ogxk")],
   [InlineKeyboardButton(text="Музыка", url="https://www.youtube.com/watch?v=0ThIonKfSHo")],
   [InlineKeyboardButton(text="Новости", url="https://www.youtube.com/watch?v=WojvsDImVTQ")],

])

test = ["Опция 1", "Опция 2"]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
   keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
   return keyboard.as_markup()

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])


