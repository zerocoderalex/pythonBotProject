import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN, API_KEY
import sqlite3


bot = Bot(token=TOKEN)
dp = Dispatcher()




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())