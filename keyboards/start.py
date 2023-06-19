from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def make_start_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать")]],
                               resize_keyboard=True)


def make_reg_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать регистрацию")]],
                               resize_keyboard=True)
