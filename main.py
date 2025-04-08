import FreeSimpleGUI as Sg



label = Sg.Text("Type in a To-Do: ")
input_box = Sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = Sg.Button("Add")

layout = [[label], [input_box, add_button]]

window = Sg.Window('My To-Do App', layout=layout)

while True:
    window.read()