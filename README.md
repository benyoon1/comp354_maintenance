# CLI To-Do Application

## Maintenance Report Submission

**Course:** COMP 354 - Introduction to Software Engineering  
**Instructor:** Dr. Malleswara Talla  
**Term:** Summer 2025

## Project Overview

This is a command-line To-Do application written in Python. It allows users to manage their tasks with features like adding, listing, searching, completing, and deleting tasks. Tasks are stored in JSON format and enhanced with features like due dates, priorities, undo functionality, and color-coded output.

## Folder Structure

```
comp354_maintenance/
├── main.py
├── task_manager.py
├── data_handler.py
├── cli_interface.py
├── undo_manager.py
├── date_manager.py
├── search_engine.py
├── priority_manager.py
├── utilities.py
├── requirements.txt
└── data/
    └── tasks.json
```

## Summary of Maintenance Contributions

- **GitHub Repository**: The project was originally not being tracked through any git or version control tools. We set up a GitHub repository to make contributions easier and to allow tracking of code changes.
- **CLI Interface Refactor**: Refactored the command-line interface from flag-based arguments (e.g., `--add`, `--list`) to a more intuitive subcommand-based structure (e.g., `add`, `list`). This follows standard CLI conventions and makes the application more user-friendly.
- **Enhanced Task Operations**: Updated `done` and `delete` commands to support both ID-based and name-based task selection using `--by-id` and `--by-name` options for greater flexibility.
- **Task Ordering Fix**: Fixed issue where tasks were displayed out of order after undo operations. Modified `get_tasks()`, `search_tasks()`, and `undo()` methods in `task_manager.py` to ensure tasks are always displayed in order of due date (earliest first) regardless of internal storage order. Tasks without due dates appear at the end, with ID as secondary sort key.
- **Improved Display Formatting**: Enhanced the command-line output formatting in `cli_interface.py` to display tasks in a clean, aligned table format with proper column headers, making the output much more readable and professional-looking.
- **Enhanced Date Display**: Improved due date formatting to be more user-friendly, showing dates in natural format (e.g., "Jul 30, 2025") with relative information like "(overdue)", "(tomorrow)", or "(2 days)" to reduce cognitive load when reading tasks using search.
- **Added Unit Tests**: Added unit tests for `cli_interface.py` and `data_handler.py`. To run all unit tests at once, refer to [Run Unit/Integration Tests](#8-run-all-unitintegration-tests).
- **Added Integration Test**: Added the integration test `test_integration.py` to simulate user workflows. It covers `add`, `done`, `delete`, `undo`, `search`, `progress`, and `list` commands in the CLI. To run the integration test, refer to [Run Unit/Integration Tests](#8-run-all-unitintegration-tests).

## Getting Started

### 1. Install Requirements

Make sure you have Python 3.7+ installed.

```bash
pip install -r requirements.txt
```

### 2. Run the Application

To run the application from PyCharm:

- Right-click on `main.py`
- Choose "Run main"
- You'll see this usage/help message:

```
usage: main.py [-h] {add,done,delete,undo,search,progress,list,help} ...

CLI To-Do Application

positional arguments:
  {add,done,delete,undo,search,progress,list,help}
    add                 Add a new task
    done                Mark task as complete
    delete              Delete task
    undo                Undo task
    search              Search Task
    progress            Show progress Task
    list                List all tasks

options:
  -h, --help            show this help message and exit
```

**IMPORTANT:** This message only shows command options. To see actual task results, you must open the Terminal tab in PyCharm and type the command directly.

## Command Usage Examples

### 1. Add a Task

```bash
python main.py add "Submit final report" --priority High --due 2025-07-15
```

### 2. List All Tasks

```bash
python main.py list
```

### 3. Mark Task as Complete

```bash
# By task ID
python main.py done --by-id 1

# By task name
python main.py done --by-name "Submit final report"
```

### 4. Delete a Task

```bash
# By task ID
python main.py delete --by-id 2

# By task name
python main.py delete --by-name "Old task"
```

### 5. Search for a Task

```bash
python main.py search report
```

### 6. Undo Last Action

```bash
python main.py undo
```

### 7. Show Task Progress

```bash
python main.py progress
```

### 8. Run All Unit/Integration Tests

```bash
cd tests
python run_tests.py
```

## Tips

- All tasks are stored in `data/tasks.json`
- Deleted tasks are temporarily saved in `data/history.json` for undo
- You can reset the task list by clearing `tasks.json`
