from os import system, path

print("Installing dependencies.")
system("pip install icalendar requests selenium==2.48")
system("pip3 install icalendar requests selenium==2.48")

print("Prepping config files.")
if not path.isfile("calendars.py"):
    with open("calendars.py") as f:
        f.write("""## Config: Put URLs to ICS endpoints in the list below.
## e.g. calendar_urls = [
##  "https://path-to-cal.com/calendar.ics",
##  "http://path-to-second-cal.com/?cal=my_cal",
## ]

calendar_urls = []
""")

if not path.isfile("db_seed.py"):
    with open("db_seed.py") as f:
        f.write("""## Config: Put URLs to username/passwords in the list below.
## e.g. seed = [{"url": "https://my-site.com/login", "username": "my-username", "password": "my-password"}]
seed = []  
""")

print("You're all set! Now, you need to configure some stuff.")
print("Write your tasks in the tasks directory!")
print("If they have credentials that you need to use, put them in db_seed.py.")
print("Configure your calendars in calendars.py!")