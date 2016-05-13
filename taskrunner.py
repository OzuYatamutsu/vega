## Runs all tasks and pushes the result to data.sqlite.
from os import getcwd, sep, listdir
from selenium import *
from datetime import datetime, time

from strings import *
from ical_parser import get_ical
from db_commit import push_data, pull_data, get_cred
from browser_utils import *

# Config
from calendars import calendar_urls
TASK_DIR = getcwd() + sep + "tasks"

# Queries
DELETE_CAL = "DELETE FROM Calendar"
UPDATE_CAL = "INSERT INTO Calendar(start_time, description) VALUES (?, ?)"
DELETE_TASKS = "DELETE FROM TaskResult"

# Task classes
IGNORE = ["task.py", "browser_task.py", "script_task.py"]

def do():
    update_calendars()
    update_tasks()
    return True
    
def update_calendars():
    for cal in calendar_urls:
        data = get_ical(cal)
        if len(data) != 0:
            print(I_CAL_CLEAR)
            push_data(DELETE_CAL)
        for event in data.keys():
            print(I_CAL_UPDATE_INSERT % (str(event), str(data[event])))
            push_data(UPDATE_CAL, (event, data[event]))
    return True
    
def update_tasks():
    push_data(DELETE_TASKS)
    for task in sorted([item for item in listdir(TASK_DIR) if item.endswith('.py') and item not in IGNORE]):
        print(I_TASK_RUN % task)
        path = TASK_DIR + sep + task
        try:
            exec(open(path).read())
            print(I_TASK_RUN_COMPLETE % task)
        except Exception as e:
            print(E_TASK_RUN_FAIL % task)
            print(e)
            continue
