# main.py
import argparse
from task_manager import TaskManager
from data_handler import DataHandler
from cli_interface import CLIInterface
from undo_manager import UndoManager


def main():

    parser = argparse.ArgumentParser(description="CLI To-Do Application")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument('--priority', type=str, choices=[
                            'High', 'Medium', 'Low'],
                            help='Set task priority', default="Medium")
    add_parser.add_argument(
        '--due', type=str, help='Set task due date (YYYY-MM-DD)')
    add_parser.add_argument("name", type=str, help='Task Names')
    done_parser = subparser.add_parser("done", help="Mark task as complete")
    done_parser.add_argument(
        "--by-id", type=int, help="Select task by id", default=-1)
    done_parser.add_argument(
        "--by-name", type=str, help="Select task by name", default="")
    delete_parser = subparser.add_parser("delete", help='Delete task')
    delete_parser.add_argument(
        "--by-id", type=int, help="Select task by id", default=-1)
    delete_parser.add_argument(
        "--by-name", type=str, help="Select task by name", default="")
    undo_parser = subparser.add_parser("undo", help='Undo task')
    search_parser = subparser.add_parser("search", help="Search Task")
    progress_parser = subparser.add_parser(
        "progress", help="Show progress Task")
    list_parser = subparser.add_parser("list", help="List all tasks")
    args = parser.parse_args()

    data_handler = DataHandler()
    undo_manager = UndoManager(data_handler)
    task_manager = TaskManager(data_handler, undo_manager)
    cli = CLIInterface()

    if args.command == "add":
        task_manager.add_task(args.name, args.priority, args.due)
    elif args.command == "done":
        task_manager.complete_task(args.by_id, args.by_name)
    elif args.command == "delete":
        task_manager.delete_task(args.by_id, args.by_name)
    elif args.command == "undo":
        task_manager.undo()
    elif args.command == "search":
        results = task_manager.search_tasks(args.search)
        cli.display_tasks(results, show_full_titles=True)
    elif args.command == "progress":
        cli.display_progress(task_manager.get_progress())
    elif args.command == "list":
        cli.display_tasks(task_manager.get_tasks())
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
