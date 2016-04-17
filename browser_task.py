## Abstract class that represents a task to be run
## using a webdriver.

from helpers import get_first_available_browser
from db_commit import pull_data, push_data
from task import Task

class BrowserTask(Task):
    def __init__(self):
        self.driver = get_first_available_browser()
    def commit_result():
        push_data("INSERT INTO TaskResult (task_file, result) VALUES (?, ?)", (self.name, self.result))
        self.driver.quit()
        return True
