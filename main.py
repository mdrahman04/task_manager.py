import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import json
from notify import check_deadline


class TaskManager(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Task Manager")
        self.configure(bg="#e1f5f4")

        # Task List
        self.tasks = []

        # Create the Task Listbox
        self.task_listbox = tk.Listbox(self, width=70, bg='#d3ede6', selectforeground='black', selectbackground='white')
        self.task_listbox.pack(padx=10, pady=10)

        # Task Entry
        self.task_entry = ttk.Entry(self, width=50)
        self.task_entry.pack(pady=(0, 5))
        self.task_entry.insert(0, "Enter Task")
        self.task_entry.bind("<FocusIn>", self.on_entry_click)
        self.task_entry.bind("<FocusOut>", self.on_exit_click)

        # Deadline Entry
        self.deadline_entry = ttk.Entry(self, width=50)
        self.deadline_entry.pack(pady=(0, 5))
        self.deadline_entry.insert(0, "Enter Deadline (dd/mm/yy HH:MM)")
        self.deadline_entry.bind("<FocusIn>", self.on_entry_click)
        self.deadline_entry.bind("<FocusOut>", self.on_exit_click)

        # Add Task Button
        add_button = ttk.Button(self, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Mark as Completed Button
        complete_button = ttk.Button(self, text="Mark as Completed", command=self.mark_completed)
        complete_button.pack(pady=5)

        # Delete Task Button
        delete_button = ttk.Button(self, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        # Save and Load Buttons
        save_button = ttk.Button(self, text="Save Tasks", command=self.save_tasks)
        save_button.pack(pady=5)
        load_button = ttk.Button(self, text="Load Tasks", command=self.load_tasks)
        load_button.pack(pady=5)

        # Help Button
        help_button = ttk.Button(self, text="Help", command=self.show_help)
        help_button.pack(pady=5)

        # Initialize the Task List
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        deadline = self.deadline_entry.get()

        if task == "Enter Task" or not task:
            messagebox.showwarning("Invalid Task", "Please enter a valid task.")
        elif deadline == "Enter Deadline (dd/mm/yy HH:MM)" or not deadline:
            messagebox.showwarning("Invalid Deadline", "Please enter a valid deadline.")
        else:
            if self.validate_date(deadline):
                self.tasks.append({"task": task, "deadline": deadline})
                self.update_task_list()
                self.clear_entry_fields()
            else:
                messagebox.showwarning("Invalid Deadline", "Please enter a valid deadline in dd/mm/yy HH:MM format.")

    def mark_completed(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            task = self.tasks[index]
            if "(Completed)" in task["task"]:
                task["task"] = task["task"].replace(" (Completed)", "")
            else:
                task["task"] += " (Completed)"

            self.update_task_list()

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"Task: {task['task']} | Deadline: {task['deadline']}")

    def clear_entry_fields(self):
        self.task_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%y %H:%M")
            return True
        except ValueError:
            return False

    def on_entry_click(self, event):
        if event.widget.get() == "Enter Task" or event.widget.get() == "Enter Deadline (dd/mm/yy HH:MM)":
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")

    def on_exit_click(self, event):
        if event.widget.get() == "":
            if event.widget == self.task_entry:
                event.widget.insert(0, "Enter Task")
            elif event.widget == self.deadline_entry:
                event.widget.insert(0, "Enter Deadline (dd/mm/yy HH:MM)")
            event.widget.config(fg="gray")

    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file)
            messagebox.showinfo("Save Tasks", "Tasks have been saved successfully.")
        except Exception as e:
            messagebox.showerror("Save Tasks", f"An error occurred while saving tasks: \n{str(e)}")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
            self.update_task_list()
            self.schedule_notifications()
            messagebox.showinfo("Load Tasks", "Tasks have been loaded successfully.")
        except FileNotFoundError:
            messagebox.showinfo("Load Tasks", "No saved tasks found.")
        except Exception as e:
            messagebox.showerror("Load Tasks", f"An error occurred while loading tasks: \n{str(e)}")

    def schedule_notifications(self):
        for task in self.tasks:
            deadline = task["deadline"]
            check_deadline(deadline, task["task"])

    def show_help(self):
        guidelines = """Welcome to Task Manager!

        Built for managing your tasks effectively.

        1. Adding Tasks:
        - Enter the task description in the 'Enter Task' field.
        - Enter Deadline using the format dd/mm/yy HH:MM.
        - Click 'Add Task' to add the task to the list.

        2. Marking as Completed:
        - Select a task from the task list.
        - Click 'Mark as Completed' when completed.
        - Click again to remove the sign.

        3. Delete Task:
        - Select a task from the task list.
        - Click 'Delete Task' to remove the task from the list.

        4. Save and Load Tasks:
        - Click 'Save Tasks' to save the current tasks to a file.
        - Click 'Load Tasks' to load tasks from a saved file.
        - If you exit without saving, the list will be
          automatically saved over existing files.

        While loading saved tasks you will be notified about
        deadlines within a day.
        """

        messagebox.showinfo("Task Manager - Help", guidelines)

    def destroy(self):
        self.save_tasks()
        tk.Tk.destroy(self)


if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
