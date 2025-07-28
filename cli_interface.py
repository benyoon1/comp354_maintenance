# cli_interface.py
from colorama import Fore, Style, init
init(autoreset=True)


class CLIInterface:
    def display_tasks(self, tasks, show_full_titles=False):
        if not tasks:
            print("No tasks found.")
            return

        if show_full_titles:
            print("\nSearch Results:")
            print("=" * 50)
            for task in tasks:
                color = self.get_color(task)
                due_date = task['due_date'] if task['due_date'] else "No due date"
                print(f"{color}ID: {task['id']}{Style.RESET_ALL}")
                print(f"{color}Title: {task['title']}{Style.RESET_ALL}")
                print(
                    f"{color}Priority: {task['priority']} | Due: {due_date} | Status: {task['status']}{Style.RESET_ALL}")
                print("-" * 50)
        else:
            print(
                f"\n{'ID':<3} | {'Title':<30} | {'Priority':<8} | {'Due Date':<12} | {'Status':<9}")
            print("-" * 70)

            for task in tasks:
                color = self.get_color(task)
                title = task['title']
                display_title = title[:27] + \
                    "..." if len(title) > 30 else title
                due_date = task['due_date'] if task['due_date'] else "No due date"

                print(
                    f"{color}{task['id']:<3} | {display_title:<30} | {task['priority']:<8} | {due_date:<12} | {task['status']:<9}{Style.RESET_ALL}")
        print()

    def display_progress(self, progress):
        completed, total = progress
        print(
            f"Completed: {completed} / {total} ({(completed/total)*100:.2f}% done)")

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
