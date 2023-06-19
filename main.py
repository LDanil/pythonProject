import db.db_funcs
import handlers.registration
from language import main
from config import TOKEN_API
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
import asyncio
from keyboards.start import *
import sqlite3
from aiogram.filters.command import Command
from aiogram.filters.text import Text
import language
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

conn = sqlite3.connect('main.db')
cur = conn.cursor()

bot = Bot(TOKEN_API)
dp = Dispatcher()


class MainStates(StatesGroup):
    check_state = State()
    reg_state = State()
    req_state = State()


@dp.message(Command("start"))
async def start_hand(message: Message):
    await message.answer(language.main.greeting, reply_markup=make_start_kb())


@dp.message(Text("Начать"))
async def check_reg(message: Message, state: FSMContext):
    await state.set_state(MainStates.check_state)

    db.db_funcs.create_db(cur, conn)
    if db.db_funcs.is_user_registered(message.from_user.id, cur):
        await message.answer(language.main.already_registered, reply_markup=ReplyKeyboardRemove())
        await state.set_state(MainStates.req_state)
    else:
        await message.answer(language.main.not_registered_yet, reply_markup=make_reg_kb())
        await state.set_state(MainStates.reg_state)
        dp.include_router(handlers.registration.reg_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
