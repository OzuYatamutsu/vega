## Abstract class that represents a task to be run
## using a webdriver.

from helpers import get_first_available_browser
from db_commit import pull_data, push_data
from tasks.task import Task

class BrowserTask(Task):
    def __init__(self, run_func, setup_func = None):
        self.driver = get_first_available_browser()
        if self.driver is None:
            raise NotImplementedError("No browsers inited to run task: " + self.name)
        self.run_func = run_func
        self.setup_func = setup_func
    def setup(self):
        if self.setup_func is None:
            raise NotImplementedError("No setup_func defined for task: " + self.name)
        self.setup_func()
    def run(self):
        if self.run_func is None:
            raise NotImplementedError("No run_func defined for task: " + self.name)
        self.run_func()
    def commit_result(self):
        push_data("INSERT INTO TaskResult (task_file, result) VALUES (?, ?)", (self.name, self.result))
        self.driver.quit()
        return True
