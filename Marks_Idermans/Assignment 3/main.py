#Marks Idermans
#mi24027

"""
Task Manager - Simple console app to manage tasks

FEATURES:
- Add tasks with priority (High/Medium/Low)
- View all tasks or only pending ones in colorful tables
- Mark tasks as done
- Delete tasks by ID
- View task statistics
- Data persists in data/tasks.txt (pipe-delimited format)

USAGE:
1.pip install rich
2.python main.py
3.Use menu to manage tasks
"""

from modules.storage import add_task, get_all_tasks, delete_task, mark_done
from modules.processor import create_task_table, get_pending_tasks, get_stats
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

console = Console()

def show_menu():
#Displays the main menu options
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. Mark Task Done")
    print("5. Delete Task")
    print("6. Stats")
    print("0. Quit")

def main():
#Main application loop
    while True:
        show_menu()
        choice = Prompt.ask("Choose option", choices=["0","1","2","3","4","5","6"])
        
        if choice == "1":
        #Add new task
            priority = Prompt.ask("Priority", choices=["High", "Medium", "Low"])
            task_desc = Prompt.ask("Task description")
            tid = add_task(priority, task_desc)
            console.print(f"[green]Added task ID {tid}[/green]")
            
        elif choice == "2":
        #Show all tasks
            tasks = get_all_tasks()
            if tasks:
                console.print(create_task_table(tasks))
            else:
                console.print("[yellow]No tasks found[/yellow]")
                
        elif choice == "3":
            # Show only pending tasks
            tasks = get_pending_tasks(get_all_tasks())
            if tasks:
                console.print(create_task_table(tasks))
            else:
                console.print("[yellow]No pending tasks[/yellow]")
                
        elif choice == "4":
        #Mark task as done
            tasks = get_all_tasks()
            if tasks:
                console.print(create_task_table(tasks))
                tid = IntPrompt.ask("Task ID to mark done")
                mark_done(str(tid))
                console.print("[green]Task marked done![/green]")
            else:
                console.print("[yellow]No tasks[/yellow]")
                
        elif choice == "5":
        #Delete task
            tasks = get_all_tasks()
            if tasks:
                console.print(create_task_table(tasks))
                tid = IntPrompt.ask("Task ID to delete")
                delete_task(str(tid))
                console.print("[red]Task deleted![/red]")
            else:
                console.print("[yellow]No tasks[/yellow]")
                
        elif choice == "6":
        #Show statistics
            tasks = get_all_tasks()
            total, pending = get_stats(tasks)
            console.print(f"[blue]Total: {total}, Pending: {pending}[/blue]")
            
        elif choice == "0":
            console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
