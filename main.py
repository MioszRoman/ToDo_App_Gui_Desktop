import FreeSimpleGUI as Sg
import os

def get_todos(filepath = 'todos.txt'):
    with open(filepath, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local

def write_todos(local_todos, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(local_todos)

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

Sg.theme("Black")
label = Sg.Text("Type in a To-Do: ")
input_box = Sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
close_button = Sg.Button("Close")
complete_button = Sg.Button("Complete")
list_box = Sg.Listbox(values=get_todos(), key='todos', size=(45, 10))

layout = [[label], [[[input_box, add_button], [list_box, edit_button, complete_button]] , [close_button]]]

window = Sg.Window('My To-Do App', layout=layout)

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            todos = get_todos()
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + '\n'
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(todos)
        case 'Complete':
            todos = get_todos()
            todo_to_complete = value['todos'][0]
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(todos)
            window['todo'].update("")
        case "Close":
            break
        case Sg.WIN_CLOSED:
            break

