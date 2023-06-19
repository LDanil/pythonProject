from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters.text import Text

import language.request
import main
from db.db_funcs import insert_client
from main import conn, cur
import language

req_router = Router()


class Requesting(StatesGroup):
    choosing_type = State()
    tech_req_chosen = State()  # Заявка на сервис
    prod_req_chosen = State()  # Заявка на товар


@req_router.message(main.MainStates.req_state)
async def make_req(message: Message, state: FSMContext):
    await message.answer(language.request.choose_type, reply_markup=)
