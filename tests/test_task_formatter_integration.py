from lib.task_formatter import TaskFormatter
from lib.task import Task

"""
Given a task, and the task is not complete,
format this task 
"""
def test_format_incomplete_task():
    task1 = Task("Walk the dog")
    task_formatter = TaskFormatter(task1)
    assert task_formatter.format() == "[ ] Walk the dog"

"""
Given a task, and the task is complete,
format this task 
"""
def test_format_complete_task():
    task1 = Task("Walk the dog")
    task1.mark_complete()
    task_formatter = TaskFormatter(task1)
    assert task_formatter.format() == "[x] Walk the dog"