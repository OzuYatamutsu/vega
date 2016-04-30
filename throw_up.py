## Outputs HTML using the result of the calendar output and task output.
from db_commit import pull_data
from strings import *
from jinhaize import jinhaize

template = ""
results = ""

print(I_THROWUP_START)
with open("template.html", 'r') as f:
    template = f.read()
for item in pull_data("SELECT task_file FROM TaskResult"):
    results = results + jinhaize(item[0])
with open("output.html", 'w') as f:
    f.writelines(template.replace("{{taskrunner-output}}", results))