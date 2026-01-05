from datetime import datetime

def add_task(task):
    with open("tasks.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(time + " - " + task + "\n")


def read_tasks():
    with open("tasks.txt", "r") as file:
        return file.readlines()
