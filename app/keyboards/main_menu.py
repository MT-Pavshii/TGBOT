from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup (
    keyboard = [
        [KeyboardButton(text = "ToDo")],
        [KeyboardButton(text = "Finance")],
        [KeyboardButton(text = "Timer")],
        [KeyboardButton(text = "/help")],
    ],
    resize_keyboard=True
)