## Abstract class that represents a task to run.

class Task:
    def __init__(self):
        self.name = __file__.split('\\')[-1]
        self.result = ""
        self.humanized_template = ""
    def setup(self):
        raise NotImplementedError
    def run(self):
        raise NotImplementedError
    def commit_result(self):
        raise NotImplementedError
