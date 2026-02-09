todo_list = {}
todo_users = set()

def enter_todo(user_id: int):
    todo_users.add(user_id)

def exit_todo(user_id: int):
    todo_users.discard(user_id)

def is_in_todo(user_id: int) -> bool:
    return user_id in todo_users

def add_item(user_id: int, item: str):
    todo_list.setdefault(user_id, []).append(item)

def get_item(user_id: int, item: str):
    return todo_list.get(user_id, [])

def remove_item(user_id: int, index: int):
    items = todo_list.get(user_id)
    if 0 <= index < len(todo_list):
        todo_list.pop(index)

