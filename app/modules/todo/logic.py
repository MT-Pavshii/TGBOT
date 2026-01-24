todo_list = []

def add_item(item: str):
    todo_list.append(item)

def get_item():
    return todo_list

def remove_item(index: int):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)