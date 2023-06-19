from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters.text import Text

import language.registration
import main
from db.db_funcs import insert_client
from main import conn, cur
import language

reg_router = Router()


class Registration(StatesGroup):
    start_reg = State()
    entering_org_state = State()
    entering_address_state = State()
    entering_name_state = State()
    entering_position_state = State()
    entering_phone_state = State()
    entering_model_state = State()


@reg_router.message(Text("Начать регистрацию"), main.MainStates.reg_state)
async def cmd_registration(message: Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    await message.answer(language.registration.enter_org, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Registration.entering_org_state)


@reg_router.message(Registration.entering_org_state, F.text)
async def org_entered(message: Message, state: FSMContext):
    await state.update_data(organization=message.text)
    await message.answer(language.registration.enter_address)
    await state.set_state(Registration.entering_address_state)


@reg_router.message(F.text, Registration.entering_address_state)
async def address_entered(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer(language.registration.enter_name)
    await state.set_state(Registration.entering_name_state)


@reg_router.message(F.text, Registration.entering_name_state)
async def name_entered(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(language.registration.enter_position)
    await state.set_state(Registration.entering_position_state)


@reg_router.message(F.text, Registration.entering_position_state)
async def position_entered(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer(language.registration.enter_phone)
    await state.set_state(Registration.entering_phone_state)


@reg_router.message(F.text, Registration.entering_phone_state)
async def phone_entered(message: Message, state: FSMContext):
    if message.entities:
        if message.entities[0].type == "phone_number":
            await state.update_data(phone=message.text)
            await state.set_state(Registration.entering_model_state)
            await message.answer(language.registration.enter_model)
        else:
            await message.answer(language.registration.wrong_phone)
    else:
        await message.answer(language.registration.wrong_phone)


@reg_router.message(F.text, Registration.entering_model_state)
async def model_entered(message: Message, state: FSMContext):
    await state.update_data(model=message.text)
    reg_data = await state.get_data()
    print(reg_data)
    await insert_client(list(reg_data.values()), cur, conn)
    await message.answer(language.registration.reg_success)
    await state.clear()
    # await main.start_hand(message)
