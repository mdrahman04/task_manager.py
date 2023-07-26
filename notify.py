from plyer import notification
from datetime import datetime, timedelta


def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )


def check_deadline(deadline, task):
    deadline_date = datetime.strptime(deadline, "%d/%m/%y %H:%M")
    current_date = datetime.now()
    one_day_before = deadline_date - timedelta(days=1)
    one_hour_before = deadline_date - timedelta(hours=1)

    if one_day_before <= current_date < deadline_date:
        show_notification("Task Reminder", f"You are 1 day away from the task: {task}")
    elif one_hour_before <= current_date < deadline_date:
        show_notification("Task Reminder", f"You are 1 hour away from the task: {task}")
