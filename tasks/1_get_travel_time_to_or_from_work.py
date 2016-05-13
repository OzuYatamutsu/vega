## Gets current travel time from home to work, or vice versa.
from datetime import datetime, time
from strings import RESULT_SEP_TOKEN
from tasks.script_task import ScriptTask
from requests import get

HUMAN_STR_1 = "Right now, it'll take about %s to get from home to work."
HUMAN_STR_2 = "Right now, it'll take about %s to get from work to home."
DIRECTION_SWITCH_THRESH = time(12, 0)
HUMAN_STR = HUMAN_STR_1 if DIRECTION_SWITCH_THRESH > datetime.time(datetime.now()) else HUMAN_STR_2

def run():
    BASE_URL = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s"
    DIRECTION_SWITCH_THRESH = time(12, 0)
    addresses, api_key = get_cred(BASE_URL)
    addresses = addresses.split(RESULT_SEP_TOKEN) # Home, work
    travel_time = {}
    if DIRECTION_SWITCH_THRESH > datetime.time(datetime.now()):
        print("Getting travel time to work.")
        travel_time = get(BASE_URL % tuple(list(reversed(addresses)))).json()
    else:
        print("Getting travel time to home.")
        travel_time = get(BASE_URL % tuple(addresses)).json()
    travel_time = travel_time["routes"][0]["legs"][0]["duration"]["text"]
    print("Travel time is %s." % travel_time)
    return (travel_time, "blue")
    
task = ScriptTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
