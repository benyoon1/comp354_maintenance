import unittest
import os
import tempfile
import shutil
from data_handler import DataHandler

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_filepath = os.path.join(self.test_dir, 'test_tasks.json')
        self.data_handler = DataHandler(self.test_filepath)
        
        self.sample_tasks = [
            {
                "id": 1,
                "title": "Test Task",
                "priority": "High",
                "due_date": "2025-07-10",
                "status": "pending"
            }
        ]

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_save_and_load_tasks(self):
        self.data_handler.save_tasks(self.sample_tasks)
        
        self.assertTrue(os.path.exists(self.test_filepath))
        
        loaded_tasks = self.data_handler.load_tasks()
        self.assertEqual(loaded_tasks, self.sample_tasks)

    def test_get_next_id_empty_list(self):
        next_id = self.data_handler.get_next_id()
        self.assertEqual(next_id, 1)

    def test_get_next_id_with_existing_tasks(self):
        self.data_handler.save_tasks(self.sample_tasks)
        next_id = self.data_handler.get_next_id()
        self.assertEqual(next_id, 2)


if __name__ == '__main__':
    unittest.main()