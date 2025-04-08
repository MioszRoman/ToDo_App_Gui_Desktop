def get_todos(filepath = 'todos.txt'):
    with open(filepath, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local

def write_todos(local_todos, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(local_todos)