from task_utils import add_task, read_tasks
from colorama import Fore, Style, init

# Initialize colorama
init()

# Add tasks
add_task("Study Python libraries")
add_task("Practice file handling")

# Print tasks in color
print(Fore.GREEN + "Task List:" + Style.RESET_ALL)

tasks = read_tasks()
for task in tasks:
    print(Fore.CYAN + task + Style.RESET_ALL)
