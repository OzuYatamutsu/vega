# Vega
**Vega** is a framework for dumping output of scripts and calendars to formatted HTML. I use it to monitor my home!
<img src="output-example.png" />

### Task flow
Writing a task with Vega has a few parts which all end with dropping your task file in the `tasks/` directory.

#### If you need a browser
* Import `BrowserTask`.
* Write a `run_func` that tells your browser what to do. It should return a result and a color (e.g. red is BAD!)
* If your task involves logging in somewhere, you can get your credentials out of sqlite by using `get_creds(url)` (see below).
* Write a `humanized_template`, which is a string template with a space for your result to be inserted (denoted by `%s`).
* End with running your task and committing the results. 

**Boilerplate example**
```python
from tasks.browser_task import BrowserTask

TEMPLATE = "The result of my task is %s. Whoo! :3"
def run(browser):
    # Do something, e.g.
    url = "https://google.com"
    browser.get(url)
    text = "Google is up!"
    return (text, "green")
task = BrowserTask(name = task, run_func = run, humanized_template = TEMPLATE)
task.run()
task.commit()
```

### If you don't need a browser
* Import `ScriptTask`.
* Write a `run_func` that performs your task. It should return a result and a color (e.g. red is BAD!)
* Write a `humanized_template`, which is a string template with a space for your result to be inserted (denoted by `%s`).
* End with running your task and committing the results. 

**Boilerplate example**

```python
from tasks.script_task import ScriptTask

TEMPLATE = "The result of my task is %s. Whoo! :3"
def run():
    # Do something, e.g.
    text = ""
    system("echo 'Myeh!' > someFile")
    with open("someFile") as f:
        text = f.read()
    return (text, "green")
task = ScriptTask(name = task, run_func = run, humanized_template = TEMPLATE)
task.run()
task.commit_result()
```

## Run 'em tasks!
```
python3 doit.py
```

When done, it'll spit out an `output.html` in your current folder.

## Database
Vega maintains a sqlite database, which holds results of tasks, calendar events, and URL credentials.

**To add calendar events to Vega**, add a URL to a public ICS file in `calendars.py`.
**To add URL credentials to Vega**, add a username, password, and the URL it will be needed at to `db_seed.py`. You will use the URL to index into the credentials table, so save it if you're writing a `BrowserTask`.

Run `db_commit.update_cred_from_seed_file()` to update the database. 

## Installation
Vega is written in Python3 and also requires **PhantomJS** to be located in your path.

We also need the following packages:

```
icalendar requests selenium==2.48
```

You can automate getting these dependencies, as well as generating `calendars.py` and `db_seed.py`, by running `python3 install.py`.
