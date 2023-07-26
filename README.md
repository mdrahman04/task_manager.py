# task_manager.py

# Task Manager User Guideline

## Introduction
This program is created with Python and allows users to manage their tasks with deadlines. With this application, one can add tasks, set deadlines, mark tasks as completed, delete/save tasks, and get notifications over deadlines. This user guideline will provide information about the basic functionality and usage of the Task Manager.

## Installation
"[commands can be directly copied and pasted without square brackets for execution]"

1. Ensure that Python is properly installed on the host system, which can be downloaded from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download and place the following files in the same directory: "main.py, notify.py, tasks.json, requirements.txt."

3. Open a terminal/command prompt and navigate to the directory where the program is saved: `[cd /path/to/the_directory]`

4. Create a virtual environment (recommended): `[python -m venv venv]`

5. Activate the virtual environment: `[source venv/bin/activate]`

6. Install the required dependencies using the "requirements.txt" file: `[pip install -r requirements.txt]`

7. Ensure that file directory location-related things are carefully handled to avoid program crashes.

## Running the Task Manager
1. Open a command prompt or terminal and navigate to the project directory.

2. Activate the virtual environment (mentioned in installation): `[source venv/bin/activate]`

3. Run the Task Manager: `[python main.py]`

4. The Task Manager application window will open.

## Adding a Task
1. In the Task Manager window, the "Enter Task" field will be visible where users can add their tasks like: "Python-Projects," "Android Studio Tutorial," "task-1," and so on.

2. The deadline for the task in the "Enter Deadline (dd/mm/yy HH:MM)" field follows a specific structure: "dd/mm/yy HH:MM". Users have to enter the date and time format as guided, else the task would not be added to the list. For example, users can type: "12/03/23 11:23," "11/2/23 4:19," or "9/7/23 05:59."

3. After correctly adding the date and task, users can click the "Add Task" button.

4. The task will be added to the task list.

## Marking a Task as Completed
1. Tasks can be selected by clicking on them from the list.

2. Clicking on the "Mark as Completed" button will put a "(completed)" sign next to the task.

3. Repeating the same process over the same task will mark it as incomplete, and the sign will be removed.

## Deleting a Task
1. After selecting a task from the task list by clicking on it, users can press the "Delete Task" button to delete the task.

2. The task will be deleted from the task list.

## Saving and Loading Tasks
1. To save the current tasks, use the "Save Tasks" button.

2. The tasks will be saved to a file named "tasks.json" in the project directory. This can overwrite the previously saved data if there was any.

3. To load saved tasks, use the "Load Tasks" button, and any remaining data on the list will be removed.

4. The tasks from the "tasks.json" file will be loaded and displayed in the task list.

5. Additionally, exiting the program directly will save the file automatically. If there was a previously saved file, and while exiting, the task list was empty or had any other data, the previous one will be replaced with the one existing on exit.

## Notifications
1. Notifications will be displayed while pressing "Load Tasks," and notifications for Python need to be enabled.

2. These notifications will be shown for tasks with a remaining time of a day or an hour from the deadline.

## Exiting the Task Manager
1. To exit the Task Manager, users can stop the program from the terminal by pressing "Ctrl+c."

2. If they are running the program from an Integrated Development Environment, they can stop running the program by "stop."

## Help Window
1. There is a "Help" button for guidelines while running the program with necessary user manual.

