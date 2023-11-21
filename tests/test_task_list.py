from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
from unittest.mock import Mock

def test_task_added_to_list_mock():
    task_list = TaskList()

    fake_task1 = Mock()
    fake_task1.title = 'Clean the shed'

    fake_task2 = Mock()
    fake_task2.title = 'Cut the grass'
    
    task_list.add(fake_task1)
    task_list.add(fake_task2)

    assert task_list.tasks == [fake_task1,fake_task2]

"""
Add a few tasks
Check to see you can see all the tasks in the list with the all method
"""
def test_task_list_returned_by_all():
    task_list = TaskList()

    fake_task1 = Mock()
    fake_task1.title = 'Clean the shed'

    fake_task2 = Mock()
    fake_task2.title = 'Cut the grass'
    
    task_list.add(fake_task1)
    task_list.add(fake_task2)

    assert task_list.all() == [fake_task1,fake_task2]

"""
Add a three tasks, and have one as complete, when calling the all_complete
method False is returned
"""
def test_three_tasks_not_all_complete():
    task_list = TaskList()

    fake_task1 = Mock()
    fake_task1.title = 'Clean the shed'
    fake_task1.is_complete.return_value = True

    fake_task2 = Mock()
    fake_task2.title = 'Cut the grass'
    fake_task2.is_complete.return_value = False

    fake_task3 = Mock()
    fake_task3.title = "Walk the dog"
    fake_task3.is_complete.return_value = False

    task_list.add(fake_task1)
    task_list.add(fake_task2)
    task_list.add(fake_task3)

    assert task_list.all_complete() == False


"""
Add a two tasks, both complete, when calling the all_complete
method True is returned
"""
def test_two_tasks_all_complete():
    task_list = TaskList()

    fake_task1 = Mock()
    fake_task1.title = 'Clean the shed'
    fake_task1.is_complete.return_value = True

    fake_task2 = Mock()
    fake_task2.title = 'Cut the grass'
    fake_task2.is_complete.return_value = True

    task_list.add(fake_task1)
    task_list.add(fake_task2)

    assert task_list.all_complete() == True

"""
Given an empty list of tasks, returns False when 
the all_complete method is called
"""
def test_empty_task_list_all_complete():
    task_list = TaskList()

    assert task_list.all_complete() == False