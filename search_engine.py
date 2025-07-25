# search_engine.py
def filter_tasks(tasks, query):
    return [task for task in tasks if query.lower() in task['title'].lower()]