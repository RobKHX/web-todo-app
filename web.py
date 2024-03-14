import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Moje aplikace Úkoly")
st.subheader("Moje první webová aplikace.")
st.write("Tato aplikace ti pomůže <b>zvýšit produktivitu</b>.",
         unsafe_allow_html=True)


st.text_input(label="", placeholder="Přidej nový úkol...: ",
              on_change=add_todo, key='new_todo')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
