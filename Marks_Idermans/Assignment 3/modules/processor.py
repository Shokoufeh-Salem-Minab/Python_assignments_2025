from rich.table import Table
from rich.console import Console

console = Console()  #Rich console for colored output

def create_task_table(tasks):
    """Creates formatted table with all tasks"""
    table = Table(title="Task Manager")
    table.add_column("ID", style="cyan")
    table.add_column("Priority", style="magenta")
    table.add_column("Task", style="white")
    table.add_column("Status", style="green")
    
    for task in tasks:
        # Truncate long tasks for display
        task_text = task['task'][:40] + "..." if len(task['task']) > 40 else task['task']
        table.add_row(task['id'], task['priority'], task_text, task['status'])
    return table

def get_pending_tasks(tasks):
    """Returns only tasks with 'Pending' status"""
    return [t for t in tasks if t['status'] == 'Pending']

def get_stats(tasks):
    """Calculates total and pending task counts"""
    total = len(tasks)
    pending = len(get_pending_tasks(tasks))
    return total, pending
