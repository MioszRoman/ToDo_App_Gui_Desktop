import FreeSimpleGUI as Sg


Sg.theme("Black")
label = Sg.Text("Type in a To-Do: ")
input_box = Sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
close_button = Sg.Button("Close")
complete_button = Sg.Button("Complete")
list_box = Sg.Listbox(values="Hello", key='todos', size=(45, 10))

layout = [[label], [[[input_box, add_button], [list_box, edit_button, complete_button]] , [close_button]]]

window = Sg.Window('My To-Do App', layout=layout)

while True:
    window.read()

