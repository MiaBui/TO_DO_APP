import streamlit as st
import Funtions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Funtions.write_todos(todos)

todos = Funtions.get_todos()

st.title("Welcome to Taskify")
st.subheader("Simple, sleek web-based to-do app for efficient task management.")
st.subheader("Stay organized and boost your productivity!!")
st.write("Here we go!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key= todo)
    if checkbox:
        todos.pop(index)
        Funtions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    

st.text_input(label="Enter your tasks need to be done", placeholder="Enter your tasks...",
              on_change= add_todo, key= "new_todo")