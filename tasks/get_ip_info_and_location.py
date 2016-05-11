## Checks current location.
from strings import RESULT_SEP_TOKEN
from tasks.script_task import ScriptTask
from requests import get

HUMAN_STR = "Our current location is %s. Current weather: %s."

def run():
    WUNDERGROUND_API_LOC = "http://api.wunderground.com/api/%s/conditions/q/autoip.json"
    api_key = get_cred(WUNDERGROUND_API_LOC)[1]
    result = get(WUNDERGROUND_API_LOC % api_key).json()
    
    location = result["current_observation"]["observation_location"]["full"]
    conditions = result["current_observation"]["weather"]
    temperature_c = str(result["current_observation"]["temp_c"]) + "\xb0C"
    temperature_f = str(result["current_observation"]["temp_f"]) + "\xb0F"

    text = location + RESULT_SEP_TOKEN + ("%s, %s" % (conditions, temperature_c))
    return (text, "blue")
    
task = ScriptTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
