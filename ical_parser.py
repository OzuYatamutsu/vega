## Given an ical link, returns a dict mapping event 
## to start time.

from requests import get
from icalendar import Calendar
from dateutil import rrule
from datetime import datetime

def get_ical(url):
    return parse_ical(get_ical_raw(url))

def get_ical_raw(url):
    data = get(url).text
    cal = Calendar.from_ical(data)
    
    return cal
    
def parse_ical(cal):
    result = {}
    for event in cal.walk('vevent'):
        name = str(event.get('summary'))
        start_time = event.get('dtstart').dt
        if event.get('rrule') is not None and len(event.get('rrule')) > 0:
            rule = event.get('rrule').to_ical().decode("utf-8")
            rrule_def = rrule.rrulestr(rule, dtstart=start_time)
            # Overwrite start_time with next
            start_time = rrule_def.after(datetime.now().replace(tzinfo=start_time.tzinfo))
        
        result[start_time] = name
    return result
