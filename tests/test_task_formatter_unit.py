from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

"""
When initially set up, 
the task property is set to the given task
"""

def test_task_property_set():
    task = Mock()
    task_formatter = TaskFormatter(task)
    assert task_formatter.task == task

"""
Given a task, and the task is not complete,
format this task 
"""
def test_format_incomplete_task():
    fake_task = Mock()
    fake_task.title = "Walk the dog"
    task_formatter = TaskFormatter(fake_task)
    fake_task.is_complete.return_value = False
    assert task_formatter.format() == "[ ] Walk the dog"
    assert fake_task.is_complete_assert_called()


"""
Given a task, and the task is complete,
format this task 
"""
def test_format_incomplete_task():
    fake_task = Mock()
    fake_task.title = "Walk the dog"
    task_formatter = TaskFormatter(fake_task)
    fake_task.is_complete.return_value = True
    assert task_formatter.format() == "[x] Walk the dog"
    assert fake_task.is_complete_assert_called()
