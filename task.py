## Abstract class that represents a task to run.

class Task:
    def __init__(self):
        self.name = __file__
        self.result = ""
    def setup():
        raise NotImplementedError
    def run():
        raise NotImplementedError
    def commit_result():
        raise NotImplementedError
