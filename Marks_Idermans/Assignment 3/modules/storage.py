import os
from pathlib import Path

#Define paths for data directory and tasks file
DATA_DIR = Path("data")
TASKS_FILE = DATA_DIR / "tasks.txt"

def ensure_data_dir():
    #Creates data directory if it doesn't exist
    DATA_DIR.mkdir(exist_ok=True)

def add_task(priority, task):
    #Adds new task to file and returns its ID
    ensure_data_dir()
    next_id = get_next_id()  # Get next available ID
    with open(TASKS_FILE, 'a') as f:  # 'a' = append mode
        f.write(f"{next_id}|{priority}|{task}|Pending\n")
    return next_id

def get_all_tasks():
    #Reads all tasks from file into list of dictionaries
    ensure_data_dir()
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as f:  # 'r' = read mode
            for line in f:
                line = line.strip()
                if line:  #Skip empty lines
                    tid, prio, task_text, status = line.split('|')
                    tasks.append({'id': tid, 'priority': prio, 'task': task_text, 'status': status})
    except FileNotFoundError:
        pass  #File doesn't exist yet
    return tasks

def delete_task(task_id):
    #Removes task with given ID by rewriting file without it
    tasks = get_all_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    rewrite_tasks(tasks)

def mark_done(task_id):
    #Updates task status to 'Done' by rewriting file
    tasks = get_all_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Done'
    rewrite_tasks(tasks)

def rewrite_tasks(tasks):
    #Overwrites entire file with current task list
    ensure_data_dir()
    with open(TASKS_FILE, 'w') as f:  # 'w' = write mode (overwrites)
        for task in tasks:
            f.write(f"{task['id']}|{task['priority']}|{task['task']}|{task['status']}\n")

def get_next_id():
    #Calculates next available task ID
    tasks = get_all_tasks()
    if not tasks:
        return "1"
    return str(max([int(t['id']) for t in tasks]) + 1)
