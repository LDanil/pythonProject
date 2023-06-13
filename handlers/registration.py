import aiogram.types.location
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.text import Text

router = Router()
data = []
r = 1


@router.message(Text("Регистация", ignore_case=True))
async def start_reg(message: Message, r):
    data.append(message.from_user.id)
    await message.answer("Введите название организации: ")


@router.message(F.Text)
async def reg_2(message: Message):
    data.append(message.text)
    await message.answer("Укажите точный адрес: ")


@router.message(F.Text)
async def reg_3(message: Message):
    data.append(message.text)
    await message.answer("Введите ФИО:")


@router.message(F.Text)
async def reg_4(message: Message):
    data.append((message.text))
    await message.answer("Введите вашу должность:")


@router.message(F.Text, f == 2)
async def reg_5(message: Message):
    data.append((message.text))
    await message.answer("Введите вашу должность:")