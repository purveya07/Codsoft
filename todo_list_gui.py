import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = TodoList()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            status = "✓" if task['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.todo_list.add_task(task)
            self.load_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.todo_list.update_task(index, new_task)
                self.load_tasks()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.complete_task(index)
            self.load_tasks()
        else:
            messagebox.showwarning("Complete Task", "Please select a task to complete.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.delete_task(index)
            self.load_tasks()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()