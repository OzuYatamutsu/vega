## Abstract class that represents a task to run.

class Task:
    def __init__(self, name):
        self.name = name
        self.result = ""
        self.humanized_template = ""
    def setup(self):
        raise NotImplementedError
    def run(self):
        raise NotImplementedError
    def commit_result(self):
        raise NotImplementedError
