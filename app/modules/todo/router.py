from aiogram import Router, types
from modules.todo.logic import add_item, get_item, remove_item, enter_todo, exit_todo, is_in_todo
from aiogram.filters import CommandStart, Command

todo_router = Router()


@todo_router.message(lambda m: m.text == "ToDo")
async def todo_entry (message: types.Message):
    enter_todo(message.from_user.id)
    await message.answer(
        "TODO:\n"
        "• Напиши задачу, чтобы добавить\n"
        "• Напиши /list чтобы увидеть все задачи\n"
        "• Напиши /done <номер> чтобы удалить задачу\n"
        "• Напиши /exit для выхода\n"
    )

@todo_router.message(lambda m: m.text and not m.text.startswith("/"))
async def add_task(message: types.Message):
    if not is_in_todo(message.from_user.id):
        return
    
    add_item(message.from_user.id, message.text)
    await message.answer(f"Задача добавлена: {message.text}")

@todo_router.message(Command ("list"))
async def list_tasks (message: types.Message):
    items = get_item(message.from_user.id)
    
    if not items:
        await message.answer ("Список пуст")
        return

    text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
    await message.answer(f"Список задач: \n{text}")

@todo_router.message(Command ("done"))
async def done_tasks (message: types.Message):
    if not is_in_todo(message.from_user.id):
        return
    
    parts = message.text.split()
    if len(parts) != 2 or not parts [1].isdigit():
        await message.answer("Используй /done <номер задачи>")
        return
    
    index = int(parts[1]) - 1
    items = get_item(message.from_user.id)
    
    if 0 <= index < len(items):
        removed = items[index]
        remove_item(message.from_user.id, index)
        await message.answer(f"Задача выполнена и удалена: {removed}")
    else:
        await message.answer("Неверный номер задачи")

@todo_router.message(Command ("exit"))
async def exit_todo_cmd(message: types.Message):
    exit_todo(message.from_user.id)
    await message.answer("Выходи из ToDo")