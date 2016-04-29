## Commits data to data.sqlite.

from sqlite3 import connect
from db_seed import seed

# Color determines how the result is rendered on the result page.
# Humanized_template determines how to display the result on the result page.
# e.g. "Your calendar says that your rent %s."
INIT_QUERIES = [
    "CREATE TABLE Calendar (start_time, description)",
    "CREATE TABLE TaskResult (task_file, result, timestamp, color, humanized_template, UNIQUE(task_file))",
    "CREATE TABLE UrlCredentials (url, username, password, UNIQUE(url))"
]
INIT_QUERY_CHECK = "SELECT name FROM sqlite_master WHERE type = 'table'"
INIT_SEED_CREDS = "INSERT OR IGNORE INTO UrlCredentials (url, username, password) VALUES ('%s', '%s', '%s')"
GET_CRED = "SELECT username, password FROM UrlCredentials WHERE url = '%s' LIMIT 1"

db = "data.sqlite"

def push_data(query, items=()):
    init_if_required()
    conn, cur = init_connection()
    
    cur.execute(query, items)
    conn.commit()
    conn.close()
    
def pull_data(query):
    init_if_required()
    if ("SELECT" in query.lower()):
        return push_data(query)
    conn, cur = init_connection()
    return cur.execute(query).fetchall()

def init_connection():
    conn = connect(db)
    cur = conn.cursor()
    
    return conn, cur
    
def get_cred(url):
    init_if_required()
    conn, cur = init_connection()
    return cur.execute(GET_CRED % url).fetchall()[0]
    
def init_if_required():
    conn, cur = init_connection()
    if len(cur.execute(INIT_QUERY_CHECK).fetchall()) == 0:
        for query in INIT_QUERIES: cur.execute(query)
    for login in seed:
        cur.execute(INIT_SEED_CREDS % (login["url"], login["username"], login["password"]))
    conn.commit()
    conn.close()
    return