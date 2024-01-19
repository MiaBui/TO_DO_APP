from Funtions import get_todos, write_todos
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print(" Today is ", now)

print("Don't waste any second!! GET ALL YOUR TASK DONE !!!")
while True:
    user_input = input("Enter add,show,edit,complete,exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = get_todos()
        todos.append(todo+ '\n')

        write_todos(todos)

    elif user_input.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f" {index + 1} - {item}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            print(number)

            number = number -1
            todos = get_todos()

            new_todo = input("Enter the new task you want to complete:")
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Please enter again!!")
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])

            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Corgartulation!!Your task {todo_to_remove} has been completed."
            print(message)
        except IndexError:
            print("Your command is not valid")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not valid. Please enter again!")

print("Goodbye!")