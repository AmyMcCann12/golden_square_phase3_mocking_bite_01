class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        if not self.task.is_complete():
            return f"[ ] {self.task.title}"
        else:
            return f"[x] {self.task.title}"
