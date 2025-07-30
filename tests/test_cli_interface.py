import unittest
from unittest.mock import patch
from io import StringIO
from cli_interface import CLIInterface

class TestCLIInterface(unittest.TestCase):
    def setUp(self):
        self.cli = CLIInterface()
        self.sample_tasks = [
            {
                "id": 1,
                "title": "Test Task 1",
                "priority": "High",
                "due_date": "2025-07-10",
                "status": "pending"
            },
            {
                "id": 2,
                "title": "Test Task 2",
                "priority": "Medium",
                "due_date": "2025-07-15",
                "status": "completed"
            }
        ]

    def test_format_due_date_valid(self):
        formatted = self.cli.format_due_date("2025-07-10")
        self.assertEqual(formatted, "Jul 10, 2025")

    def test_format_due_date_none(self):
        formatted = self.cli.format_due_date(None)
        self.assertEqual(formatted, "No due date")

    def test_format_due_date_invalid_format(self):
        formatted = self.cli.format_due_date("invalid-date")
        self.assertEqual(formatted, "invalid-date")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_tasks_empty(self, mock_stdout):
        self.cli.display_tasks([])
        output = mock_stdout.getvalue()
        self.assertIn("No tasks found.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_tasks_table_format(self, mock_stdout):
        self.cli.display_tasks(self.sample_tasks)
        output = mock_stdout.getvalue()
        
        self.assertIn("ID", output)
        self.assertIn("Title", output)
        self.assertIn("Priority", output)
        self.assertIn("Due Date", output)
        self.assertIn("Status", output)
        self.assertIn("Test Task 1", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_progress(self, mock_stdout):
        self.cli.display_progress((3, 10))
        output = mock_stdout.getvalue()
        
        self.assertIn("Completed: 3 / 10", output)
        self.assertIn("30.00%", output)

if __name__ == '__main__':
    unittest.main()