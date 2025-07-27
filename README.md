# CLI To-Do Application

## Maintenance Report Submission

**Course:** COMP 354 Introduction to Software Engineering  
**Instructor:** Dr. Malleswara Talla  
**Term:** Summer 2 2025

### Team Members

1. Nidhi Prasad (40259273)
2. Narendra Mishra (40224303)
3. Neelendra Mishra (40224310)
4. Aryan Kotecha (40249867)
5. Parsa Ghadimi (40203370)
6. Kirubel Asrat (40153970)

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
usage: main.py [-h] [--add ADD] [--priority {High,Medium,Low}] [--due DUE]
               [--done DONE] [--delete DELETE] [--list] [--undo]
               [--search SEARCH] [--progress]

CLI To-Do Application

optional arguments:
  -h, --help            show this help message and exit
  --add ADD             Add a new task
  --priority {High,Medium,Low}  Set task priority
  --due DUE             Set task due date (YYYY-MM-DD)
  --done DONE           Mark task as complete
  --delete DELETE       Delete task by ID
  --list                List all tasks
  --undo                Undo last action
  --search SEARCH       Search tasks
  --progress            Show task progress

Process finished with exit code 0
```

**IMPORTANT:** This message only shows command options. To see actual task results, you must open the Terminal tab in PyCharm and type the command directly.

## Command Usage Examples

### 1. Add a Task

```bash
python main.py --add "Submit final report" --priority High --due 2025-07-15
```

### 2. List All Tasks

```bash
python main.py --list
```

### 3. Mark Task as Complete

```bash
python main.py --done 1
```

### 4. Delete a Task

```bash
python main.py --delete 2
```

### 5. Search for a Task

```bash
python main.py --search report
```

### 6. Undo Last Action

```bash
python main.py --undo
```

### 7. Show Task Progress

```bash
python main.py --progress
```

## Tips

- All tasks are stored in `data/tasks.json`
- Deleted tasks are temporarily saved in `data/history.json` for undo
- You can reset the task list by clearing `tasks.json`

---

Thanks
