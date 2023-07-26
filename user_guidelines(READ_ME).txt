# Task Manager User Guideline #

## Introduction
This program is created with Python and allow the users to manage their tasks with deadlines. With this application, one can add tasks, set deadlines, mark tasks as completed, delete/save tasks and get notifications over deadlines. This user guideline will provide information about the basic functionality and usage of the Task Manager.



*** Installation ***
"[commands can be directly copied and pasted without square brackets for execution]"

1. Most importantly, the user has to ensure Python installation has been done properly on the host system, which can be downloaded from the official website: https://www.python.org/downloads/

2. Next step is to make sure the files "main.py, notify.py, tasks.json, requirements.txt" are on the same directory and downloaded properly.

3. Then, a terminal/command_prompt needs to be opened on the host device and users have to navigate [cd /path/to/the_directory] to the directory where the program is saved.

4. After going to the specific directory, user has to create a virtual environment (recommended): [python -m venv venv]

5. Then the virtual environment needs to be activated. The virtual environment activation command: [source venv/bin/activate]

6. There are multiple dependencies to run the program and these need to be installed to avoid launch failure. To install the required dependencies the "dependencies.txt" file is required and the command is: [pip install -r requirements.txt]

7. File directory location related things should be carefully handled, otherwise the program might crash.



## Running the Task Manager
1. After opening a command prompt or terminal, user has to navigate to the project directory.
2. Then, activate the virtual environment (mentioned in installation): [source venv/bin/activate]
3. User can then run the Task Manager by: [python main.py]
4. The Task Manager application window will open.

## Adding a Task
1. In the Task Manager window, "Enter Task" field will be visible where users can add there tasks like: "Python-Projects", "Android Studio Tutorial", "task-1" and so on.
2. The deadline for the task in the "Enter Deadline (dd/mm/yy HH:MM)" field follows a special structure and users have to enter date and time format specifically in "dd/mm/yy HH:MM" format as guided, else the task would not be added in the list. For an instance user can type: "12/03/23 11:23", "11/2/23 4:19" or "9/7/23 05:59".
3. After, correctly adding the date and task user can click the "Add Task" button.
4. The task will be added to the task list.

## Marking a Task as Completed
1. Tasks can be selected by clicking over them from the list.
2. After that, clicking on the "Mark as Completed" button will put a "(completed)" sign next to the task.
3. Repeating the same process over the same task will mark it as incomplete and the sign will be removed.

## Deleting a Task
1. After, selecting a task from the task list by clicking on it users can press on the "Delete Task" button to delete the task.
3. The task will be deleted from the task list.

## Saving and Loading Tasks
1. To save the current tasks, "Save Tasks" button can be used.
2. The tasks will be saved to a file named "tasks.json" in the project directory. And, this can rewrite over the previously saved data if there was any.
3. To load saved tasks, "Load Tasks" button can be used and any remaining data on the list will be removed.
4. The tasks from the "tasks.json" file will be loaded and displayed in the task list.
5. Additionally, exiting the program directly will save the file automatically. And, in this case if there was a previously saved file and while exiting the task list was empty or had any other data the previous one will be replaced with the one existing on exit.

## Notifications
1. Notifications will be displayed while pressing load tasks and notifications for python needs to be enabled.
2. These will be shown for tasks with a remaining time of a day or an hour from the deadline.

## Exiting the Task Manager
1. To exit the Task Manager, users can stop the program from terminal by pressing "Ctrl+c"
2. If they are running the program from a Integrated Development Environment they can stop running the program by "stop".

## Help Window
1. There is a "Help" button for guidelines while running the program with necessary user manual.