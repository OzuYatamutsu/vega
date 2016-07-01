## Takes a screenshot of the desktop.
from strings import RESULT_SEP_TOKEN
from tasks.script_task import ScriptTask
from requests import get
from os import system

BASE_FOLDER = "/var/www/html/vega/"
IMAGE_FOLDER = "images/"
HUMAN_STR = "Here's what the desktop looks like: " + '<a href="' + IMAGE_FOLDER + '%s"><img src="' + IMAGE_FOLDER + '%s" /></a>'

def run():
    system("bash -c 'DISPLAY=:10 scrot /var/www/html/status/test.png'")
    # TODO: stubbed
    text = ""
    return ("", "black")
    
#task = ScriptTask(name = task, run_func = run, humanized_template = HUMAN_STR)
#task.run()
#task.commit_result()
