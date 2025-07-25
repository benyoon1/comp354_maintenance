# main.py
import argparse
from task_manager import TaskManager
from data_handler import DataHandler
from cli_interface import CLIInterface
from undo_manager import UndoManager


def main():
    parser = argparse.ArgumentParser(description="CLI To-Do Application")
    parser.add_argument('--add', type=str, help='Add a new task')
    parser.add_argument('--priority', type=str, choices=['High', 'Medium', 'Low'], help='Set task priority')
    parser.add_argument('--due', type=str, help='Set task due date (YYYY-MM-DD)')
    parser.add_argument('--done', type=int, help='Mark task as complete')
    parser.add_argument('--delete', type=int, help='Delete task by ID')
    parser.add_argument('--list', action='store_true', help='List all tasks')
    parser.add_argument('--undo', action='store_true', help='Undo last action')
    parser.add_argument('--search', type=str, help='Search tasks')
    parser.add_argument('--progress', action='store_true', help='Show task progress')

    args = parser.parse_args()

    data_handler = DataHandler()
    undo_manager = UndoManager(data_handler)
    task_manager = TaskManager(data_handler, undo_manager)
    cli = CLIInterface()

    if args.add:
        task_manager.add_task(args.add, args.priority, args.due)
    elif args.done:
        task_manager.complete_task(args.done)
    elif args.delete:
        task_manager.delete_task(args.delete)
    elif args.undo:
        task_manager.undo()
    elif args.search:
        results = task_manager.search_tasks(args.search)
        cli.display_tasks(results)
    elif args.progress:
        cli.display_progress(task_manager.get_progress())
    elif args.list:
        cli.display_tasks(task_manager.get_tasks())
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
