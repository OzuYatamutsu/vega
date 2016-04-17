## Given an ical link, returns a dict mapping event 
## to start time.

from requests import get
from icalendar import Calendar

def get_ical(url):
    data = get(url).text
    cal = Calendar.from_ical(data)
    
    return parse_ical(cal)
    
def parse_ical(cal):
    result = {}
    for event in cal.walk('vevent'):
        name = str(event.get('summary'))
        start_time = event.get('dtstart').dt
        
        result[start_time] = name
    return result