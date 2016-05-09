## Abstract class that represents a task to be run
## as a Python script or on the shell.
from db_commit import pull_data, push_data
from tasks.task import Task
from strings import *
from time import time

class ScriptTask(Task):
    def __init__(self, name, run_func, humanized_template, setup_func = None):
        Task.__init__(self, name)
        self.run_func = run_func
        self.humanized_template = humanized_template
        self.setup_func = setup_func
        self.result = None
    def setup(self):
        if self.setup_func is None:
            raise NotImplementedError(E_SCRIPTTASK_NO_SETUP_FUNC % self.name)
        self.setup_func()
    def run(self):
        if self.run_func is None:
            raise NotImplementedError(E_SCRIPTTASK_NO_RUN_FUNC % self.name)
        self.result = self.run_func()
    def commit_result(self):
        timestamp = str(time())
        print(I_SCRIPTTASK_COMMIT % (self.result, timestamp))
        push_data("INSERT OR REPLACE INTO TaskResult (task_file, result, timestamp, color, humanized_template) VALUES (?, ?, ?, ?, ?)", (self.name, self.result[0], timestamp, self.result[1], self.humanized_template))
        return True
