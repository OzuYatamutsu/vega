## Outputs HTML using the result of the calendar output and task output.
from db_commit import pull_data
from strings import *
from jinhaize import jinhaize, jinhaize_event

def main():
    template = ""
    results = ""
    events = ""
    print(I_THROWUP_START)
    with open("template.html", 'r') as f:
        template = f.read()
    for item in pull_data("SELECT task_file FROM TaskResult"):
        results = results + jinhaize(item[0])
    next_event = pull_data("SELECT * FROM Calendar ORDER BY start_time ASC LIMIT 1")[0]
    events = jinhaize_event(next_event)
    with open("output.html", 'w') as f:
        f.writelines(template.replace("{{taskrunner-output}}", results).replace("{{calendar-output}}", events))