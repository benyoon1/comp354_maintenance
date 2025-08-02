import unittest
import os
import tempfile
import shutil
from unittest.mock import patch

from task_manager import TaskManager
from data_handler import DataHandler
from cli_interface import CLIInterface
from undo_manager import UndoManager

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        # make temp data for testing. will be deleted in tearDown
        self.test_dir = tempfile.mkdtemp()
        self.data_file = os.path.join(self.test_dir, 'tasks.json')
        self.history_file = os.path.join(self.test_dir, 'history.json')
        
        self.data_handler = DataHandler(self.data_file)
        self.undo_manager = UndoManager(self.data_handler)
        self.undo_manager.history_path = self.history_file
        self.task_manager = TaskManager(self.data_handler, self.undo_manager)
        self.cli = CLIInterface()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    @patch('builtins.print')
    def test_user_workflow(self, mock_print):
        # user adds tasks
        self.task_manager.add_task("Buy groceries", "High", "2025-07-15")
        self.task_manager.add_task("Study for exam", "Medium", "2025-07-20")
        self.task_manager.add_task("Call dentist", "Low", "2025-07-10")
        self.task_manager.add_task("Weekend project", "Medium", None)
        
        # user lists all tasks. should be sorted by due date
        tasks = self.task_manager.get_tasks()
        self.assertEqual(len(tasks), 4)
        self.assertEqual(tasks[0]["title"], "Call dentist")
        self.assertEqual(tasks[1]["title"], "Buy groceries")
        self.assertEqual(tasks[2]["title"], "Study for exam")
        self.assertEqual(tasks[3]["title"], "Weekend project")

        # user searches for specific tasks
        grocery_tasks = self.task_manager.search_tasks("groceries")
        self.assertEqual(len(grocery_tasks), 1)
        self.assertEqual(grocery_tasks[0]["title"], "Buy groceries")

        # user completes some tasks
        self.task_manager.complete_task(-1, "Call dentist")  # pass invalid ID -1 to use name
        self.task_manager.complete_task(1, "")  # find by ID

        # user checks progress
        completed, total = self.task_manager.get_progress()
        self.assertEqual(completed, 2)
        self.assertEqual(total, 4)

        # user deletes a task
        self.task_manager.delete_task(-1, "Study for exam")
        tasks_after_delete = self.task_manager.get_tasks()
        self.assertEqual(len(tasks_after_delete), 3)

        # user undoes deletion
        self.task_manager.undo()
        tasks_after_undo = self.task_manager.get_tasks()
        self.assertEqual(len(tasks_after_undo), 4)
        
        # verify restore
        study_task = next(t for t in tasks_after_undo if t["title"] == "Study for exam")
        self.assertEqual(study_task["priority"], "Medium")
        self.assertEqual(study_task["due_date"], "2025-07-20")


if __name__ == '__main__':
    unittest.main()