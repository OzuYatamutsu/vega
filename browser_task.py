## Abstract class that represents a task to be run
## using a webdriver.

from helpers import get_first_available_browser
from db_commit import pull_data, push_data
from task import Task

class BrowserTask(Task):
    def __init__(self, run_func, setup_func = None):
        self.driver = get_first_available_browser()
        self.run_func = run_func
        self.setup_func = setup_func
    def setup():
        if setup_func is None:
            raise NotImplementedError("No setup_func defined for task: " + self.name)
        this.setup_func()
    def run():
        if run_func is None:
            raise NotImplementedError("No run_func defined for task: " + self.name)
        this.run_func()
    def commit_result():
        push_data("INSERT INTO TaskResult (task_file, result) VALUES (?, ?)", (self.name, self.result))
        self.driver.quit()
        return True
