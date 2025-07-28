# cli_interface.py
from colorama import Fore, Style, init
from datetime import datetime, timedelta
init(autoreset=True)


class CLIInterface:
    def format_due_date(self, due_date_str, show_relative=False):
        """Format due date to be more human-readable with optional relative information"""
        if not due_date_str:
            return "No due date"

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            today = datetime.now().date()
            due_date_only = due_date.date()

            formatted_date = due_date.strftime(
                "%b %d, %Y")  # e.g., "Jul 10, 2025"

            # add relative information only if requested
            if show_relative:
                days_diff = (due_date_only - today).days

                if days_diff < 0:
                    return f"{formatted_date} (overdue)"
                elif days_diff == 0:
                    return f"{formatted_date} (today)"
                elif days_diff == 1:
                    return f"{formatted_date} (tomorrow)"
                elif days_diff <= 7:
                    return f"{formatted_date} ({days_diff} days)"

            return formatted_date

        except ValueError:
            return due_date_str  # return original if parsing fails

    def display_tasks(self, tasks, show_full_titles=False):
        if not tasks:
            print("No tasks found.")
            return

        if show_full_titles:
            print("\nSearch Results:")
            print("=" * 50)
            for task in tasks:
                color = self.get_color(task)
                due_date = self.format_due_date(
                    task['due_date'], show_relative=True)
                print(f"{color}ID: {task['id']}{Style.RESET_ALL}")
                print(f"{color}Title: {task['title']}{Style.RESET_ALL}")
                print(
                    f"{color}Priority: {task['priority']} | Due: {due_date} | Status: {task['status']}{Style.RESET_ALL}")
                print("-" * 50)
        else:
            print(
                f"\n{'ID':<3} | {'Title':<30} | {'Priority':<8} | {'Due Date':<15} | {'Status':<9}")
            print("-" * 73)

            for task in tasks:
                color = self.get_color(task)
                title = task['title']
                display_title = title[:27] + \
                    "..." if len(title) > 30 else title
                due_date = self.format_due_date(
                    task['due_date'], show_relative=False)
                # truncate due date if too long for table
                display_due = due_date[:13] + \
                    ".." if len(due_date) > 15 else due_date

                print(
                    f"{color}{task['id']:<3} | {display_title:<30} | {task['priority']:<8} | {display_due:<15} | {task['status']:<9}{Style.RESET_ALL}")
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
