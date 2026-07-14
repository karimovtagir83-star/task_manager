import task
import json
import os


tasks = []


def add_task(title, description):
    tasks.append(task.Task(title, description))
    print("The task has been added.")


def list_tasks():
    if not tasks:
        print("No tasks.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.complete else "Pending"
        print(f"""
Index: {index}
Task: {task.title}
Description: {task.description}
Status: {status}
""")


def delete_task(argument):
    if argument == "all":
        tasks.clear()
        print("All tasks have been deleted.")
        return
    for task in tasks:
        if task.title == argument:
            tasks.remove(task)
            print("The task has been deleted.")
            return
    print("Task not found.")


def complete_task(argument):
    if argument == "all":
        for task in tasks:
            task.complete = True
        print("The status of all tasks has been changed to completed.")
        return
    for task in tasks:
        if task.title == argument:
            task.complete = True
            print("The task status has been changed to completed.")
            return
    print("Task not found.")


def save_tasks():
    data = []
    for task in tasks:
        intojson = {
            "title": task.title,
            "description": task.description,
            "complete": task.complete
        }
        data.append(intojson)
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_tasks():
    if not os.path.exists("tasks.json"):
        return
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []
    for item in data:
        new_task = task.Task(
            item["title"],
            item["description"],
            item["complete"]
        )
        tasks.append(new_task)