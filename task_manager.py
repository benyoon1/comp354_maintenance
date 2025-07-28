# task_manager.py
from datetime import datetime
from priority_manager import validate_priority
from date_manager import validate_date, is_due_soon
from search_engine import filter_tasks


class TaskManager:
    def __init__(self, data_handler, undo_manager):
        self.data_handler = data_handler
        self.undo_manager = undo_manager
        self.tasks = self.data_handler.load_tasks()

    def add_task(self, title, priority='Medium', due_date=None):
        if not validate_priority(priority):
            print("Invalid priority.")
            return

        if due_date and not validate_date(due_date):
            print("Invalid due date format.")
            return

        task = {
            "id": self.data_handler.get_next_id(),
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "status": "pending",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_date": None
        }
        self.tasks.append(task)
        self.data_handler.save_tasks(self.tasks)
        print("Task added.")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id and task["status"] == "pending":
                task["status"] = "completed"
                task["completed_date"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")
                self.data_handler.save_tasks(self.tasks)
                print("Task marked as complete.")
                return
        print("Task not found or already completed.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.undo_manager.backup(task)
                del self.tasks[i]
                self.data_handler.save_tasks(self.tasks)
                print("Task deleted.")
                return
        print("Task not found.")

    def search_tasks(self, query):
        results = filter_tasks(self.tasks, query)
        return sorted(results, key=lambda x: x['id'])

    def get_tasks(self):
        return sorted(self.tasks, key=lambda x: x['id'])

    def get_progress(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["status"] == "completed"])
        return completed, total

    def undo(self):
        restored = self.undo_manager.restore()
        if restored:
            self.tasks.append(restored)
            self.tasks.sort(key=lambda x: x['id'])
            self.data_handler.save_tasks(self.tasks)
            print("Undo successful.")
        else:
            print("Nothing to undo.")
