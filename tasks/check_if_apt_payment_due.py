## Checks if my apartment payment is due.
from tasks.browser_task import BrowserTask

def run():
    print("TODO: Stubbed test")
    return 1
    
task = BrowserTask(run_func = run)
task.run()