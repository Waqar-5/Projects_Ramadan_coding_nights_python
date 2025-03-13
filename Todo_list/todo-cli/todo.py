import streamlit as st
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Load tasks initially
tasks = load_tasks()

st.title("📝 Simple To-Do List Manager")

# Input for adding new tasks
new_task = st.text_input("Enter a new task:")
if st.button("➕ Add Task"):
    if new_task.strip():
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.rerun()  # Refresh the page

# Display tasks
st.subheader("Your Tasks:")
if not tasks:
    st.write("No tasks found.")
else:
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([4, 1, 1])
        col1.write(f"**{index + 1}. {task['task']}**")
        
        if col2.button("✅ Complete", key=f"complete_{index}"):
            tasks[index]["done"] = True
            save_tasks(tasks)
            st.rerun()
        
        if col3.button("❌ Remove", key=f"remove_{index}"):
            tasks.pop(index)
            save_tasks(tasks)
            st.rerun()
