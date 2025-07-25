# date_manager.py
from datetime import datetime, timedelta

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_due_soon(date_str, days_ahead=3):
    due = datetime.strptime(date_str, "%Y-%m-%d")
    return datetime.now().date() <= due.date() <= (datetime.now() + timedelta(days=days_ahead)).date()

