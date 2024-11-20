import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the main application
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x600")
root.config(bg="#f0f0f5")

# List to store tasks
tasks = []

# Function to update the task list
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        task_list.insert(tk.END, f"{status} {task['title']} - {task['priority']}")

# Add a new task
def add_task():
    title = task_entry.get()
    priority = priority_combobox.get()
    if title and priority:
        tasks.append({"title": title, "priority": priority, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
        priority_combobox.set("")
    else:
        messagebox.showwarning("Input Error", "Please enter a task and select a priority!")

# Mark a task as completed
def mark_completed():
    selected_task = task_list.curselection()
    if selected_task:
        tasks[selected_task[0]]["completed"] = not tasks[selected_task[0]]["completed"]
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Delete a task
def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_task_list()

# Header
header_frame = tk.Frame(root, bg="#4caf50", pady=10)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#4caf50", fg="white")
header_label.pack()

# Task Input Frame
input_frame = tk.Frame(root, bg="#f0f0f5", pady=10)
input_frame.pack(fill=tk.X, padx=10)
task_label = tk.Label(input_frame, text="Task:", bg="#f0f0f5", font=("Helvetica", 12))
task_label.grid(row=0, column=0, padx=5, sticky="w")
task_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=25)
task_entry.grid(row=0, column=1, padx=5)
priority_label = tk.Label(input_frame, text="Priority:", bg="#f0f0f5", font=("Helvetica", 12))
priority_label.grid(row=1, column=0, padx=5, sticky="w")
priority_combobox = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], font=("Helvetica", 12), state="readonly")
priority_combobox.grid(row=1, column=1, padx=5)
add_button = tk.Button(input_frame, text="Add Task", font=("Helvetica", 12), bg="#4caf50", fg="white", command=add_task)
add_button.grid(row=0, column=2, rowspan=2, padx=5)

# Task List
task_list_frame = tk.Frame(root, bg="#f0f0f5")
task_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
task_list = tk.Listbox(task_list_frame, font=("Helvetica", 12), height=15, selectmode=tk.SINGLE, bg="white", fg="#333", bd=2, relief=tk.SUNKEN)
task_list.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
scrollbar = tk.Scrollbar(task_list_frame, orient=tk.VERTICAL, command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f5", pady=10)
button_frame.pack(fill=tk.X)
mark_button = tk.Button(button_frame, text="Mark Completed", font=("Helvetica", 12), bg="#2196f3", fg="white", command=mark_completed)
mark_button.grid(row=0, column=0, padx=10)
delete_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 12), bg="#f44336", fg="white", command=delete_task)
delete_button.grid(row=0, column=1, padx=10)
clear_button = tk.Button(button_frame, text="Clear All", font=("Helvetica", 12), bg="#ff9800", fg="white", command=clear_tasks)
clear_button.grid(row=0, column=2, padx=10)

# Footer
footer_label = tk.Label(root, text="Organize your tasks with ease!", bg="#f0f0f5", font=("Helvetica", 10, "italic"), fg="#555")
footer_label.pack(side=tk.BOTTOM, pady=5)

# Run the application
root.mainloop()
