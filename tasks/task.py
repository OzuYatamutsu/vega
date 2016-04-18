## Abstract class that represents a task to run.

class Task:
    def __init__(self):
        self.name = __file__
        self.result = ""
    def setup(self):
        raise NotImplementedError
    def run(self):
        raise NotImplementedError
    def commit_result(self):
        raise NotImplementedError
