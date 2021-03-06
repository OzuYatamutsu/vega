## Constructs an HTML string from a template, result, and color.
from db_commit import pull_data
from datetime import datetime
from time import ctime
from strings import RESULT_SEP_TOKEN

QUERY = "SELECT timestamp, result, humanized_template, color FROM TaskResult WHERE task_file = '%s' LIMIT 1"

def jinhaize(task_file):
    data = pull_data(QUERY % task_file)[0]
   
    timestamp = ctime(float(data[0]))
    results = data[1].split(RESULT_SEP_TOKEN)
    humanized_template = data[2]
    color = data[3]    
    formatted_results = []

    for index in range(0, len(results)):
        formatted_results.append(('<font color="%s"><strong>%s</strong></font>' \
            % tuple([color, results[index]])))
    return (humanized_template % tuple(formatted_results)) + (" (Last updated %s)" % timestamp)

def jinhaize_event(calendar_event): 
    timestamp = calendar_event[0]
    event_title = calendar_event[1]
    dt_timestamp = datetime.strptime(timestamp.split(" ")[0], '%Y-%m-%d')
    
    return ('In <strong>%s</strong>: Your next event is <font color="blue"><strong>%s</strong></font> on <font color="blue">%s</font>.') % \
    (humanize_tz_delta_days(dt_timestamp), event_title, timestamp.split(" ")[0])

def humanize_tz_delta_days(dt):
    delta = dt - datetime.now()
    num_days = delta.days + 1 # Correct off-by-one error
    return "1 day" if num_days == 1 else ("%s days" % num_days)
