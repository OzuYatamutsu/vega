## Checks current location.
from tasks.script_task import ScriptTask
from requests import get

HUMAN_STR = "Our IP address is %s, which puts us in %s. The current weather: %s."

def run():
    ip_response = get("ipinfo.io").json()
    weather_response = get("").json()    

return (text, "green" if float(text.replace("$", "").replace(",", "")) <= 0.0 else "red")  
    print("Amount due: " + text)
    
task = ScriptTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
