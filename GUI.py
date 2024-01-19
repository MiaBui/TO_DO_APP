import Funtions
import PySimpleGUI

label = PySimpleGUI.Text(" Enter your tasks need to be done:")
input_box = PySimpleGUI.InputText(tooltip="Enter your tasks", key="todo")

add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=Funtions.get_todos(), key= "todos",
                               enable_events=True, size=(40, 20))
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")

window = PySimpleGUI.Window("Taskify",
                            layout=[[label],
                                    [input_box, add_button],
                                    [list_box, edit_button],
                                    [complete_button]],
                            font=('Roboto', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)

    match event:
        case "Add":
            todos = Funtions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Funtions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = Funtions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            Funtions.write_todos(todos)
            window['todos'].update(values=todos)
            PySimpleGUI.popup("Your tasks has been updated!")
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = Funtions.get_todos()
            todos.remove(todo_to_complete)
            Funtions.write_todos(todos)
            window['todos'].update(values=todos)
            PySimpleGUI.popup("Congrad!! You did a good job!")

        case PySimpleGUI.WIN_CLOSED:
            break

print('Good Bye')
window.close()

