## Constructs an HTML string from a template, result, and color.
from db_commit import pull_data
from time import ctime

QUERY = "SELECT timestamp, result, humanized_template, color FROM TaskResult WHERE task_file = '%s' LIMIT 1"

def jinhaize(task_file):
    data = pull_data(QUERY % task_file)[0]
    
    timestamp = ctime(float(data[0]))
    result = data[1]
    humanized_template = data[2]
    color = data[3]
    
    return (humanized_template % \
        ('<font color="%s"><strong>%s</strong></font>' % (color, result)) \
        ) + (" (Last updated %s)" % timestamp)

def jinhaize_event(calendar_event):
    timestamp = calendar_event[0]
    event_title = calendar_event[1]
    
    return ('Your next event is <font color="blue"><strong>%s</strong></font> at <font color="blue">%s</font>.') % (event_title, timestamp)