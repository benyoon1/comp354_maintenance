# undo_manager.py
import json
import os

class UndoManager:
    def __init__(self, data_handler):
        self.history_path = 'data/history.json'
        self.data_handler = data_handler
        os.makedirs('data', exist_ok=True)

    def backup(self, task):
        with open(self.history_path, 'w') as f:
            json.dump(task, f)

    def restore(self):
        if not os.path.exists(self.history_path):
            return None
        with open(self.history_path, 'r') as f:
            task = json.load(f)
        os.remove(self.history_path)
        return task
