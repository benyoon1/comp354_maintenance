# cli_interface.py
from colorama import Fore, Style, init
init(autoreset=True)

class CLIInterface:
    def display_tasks(self, tasks):
        for task in tasks:
            color = self.get_color(task)
            print(f"{color}ID: {task['id']} | {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {task['status']}{Style.RESET_ALL}")

    def display_progress(self, progress):
        completed, total = progress
        print(f"Completed: {completed} / {total} ({(completed/total)*100:.2f}% done)")

    def get_color(self, task):
        if task["status"] == "completed":
            return Fore.GREEN
        if task["due_date"]:
            from datetime import datetime
            due = datetime.strptime(task["due_date"], "%Y-%m-%d")
            if due < datetime.now():
                return Fore.RED
        if task["priority"] == "High":
            return Fore.YELLOW
        elif task["priority"] == "Medium":
            return Fore.BLUE
        return Fore.WHITE
