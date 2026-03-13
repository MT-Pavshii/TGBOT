from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from keyboards.main_menu import main_menu_kb
from data import db

user_private_router = Router() # при присвоении класса не забывай ставить скобки

@user_private_router.message(CommandStart()) # это хендлер благодоря которому мы прописываем функции боту
async def start_cmd(message: types.Message):
    db.add_users(
        message.from_user.id,
        message.from_user.username
    )
    await message.answer("Выбери функцию", reply_markup = main_menu_kb)

@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Ботик создан для повседневности в нем имеются:\n1.To Do лист\n2.Бухгалтерия\n3.Умный таймер")

@user_private_router.message(lambda m: m.text == "Timer")
async def timer_entry(message: types.Message):
    await message.answer(
        "Таймер:\n"
        "• Общее время\n"
        "• Интервалы работы\n"
        "• Паузы\n\n"
        "Скоро будет 👀"
    )

@user_private_router.message(Command('drop'))
async def drop_cmd(message: types.Message):
    await message.answer("DROPDROPDROP")    




