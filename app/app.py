import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from bot_commands import bot_commands

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from modules.todo.router import todo_router

ALLOWED_UPDATES = ["message", "edited_massage"] # переменная которая ограничевает обработку входящих данных

bot = Bot(token = os.getenv('TOKEN')) # токен отвечающий за коннект с ботом
dp = Dispatcher() # переменная связанная с обьектом который позволяет создавать хэндлеры 

dp.include_router(user_private_router)
dp.include_router(todo_router)    

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await bot.set_my_commands(bot_commands)
    await dp.start_polling(bot, allowed_updates = ALLOWED_UPDATES)
asyncio.run(main())