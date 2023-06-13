import datetime
import db_defs
from config import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types
from db.db_funcs import *
import sqlite3

conn = sqlite3.connect('main.db')
cur = conn.cursor()

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_hand(message: types.Message):
    await message.answer("Start")

if __name__ == '__main__':
    executor.start_polling(dp)
