## Abstract class that represents a task to run.

# Note: if returning more than one result, separate 
# results with strings.RESULT_SEP_TOKEN.
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
