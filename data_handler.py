# data_handler.py
import json
import os

class DataHandler:
    def __init__(self, filepath='data/tasks.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def load_tasks(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save_tasks(self, tasks):
        with open(self.filepath, 'w') as f:
            json.dump(tasks, f, indent=4)

    def get_next_id(self):
        tasks = self.load_tasks()
        return max((task['id'] for task in tasks), default=0) + 1