from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def make_choice_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Сервис")],
        [KeyboardButton(text="Товар")]
    ],
        resize_keyboard=True)


def make_confirm_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Отменить отправку")],
        [KeyboardButton(text="Все верно, отправить запрос")]
    ],
        resize_keyboard=True)
