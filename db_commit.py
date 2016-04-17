## Commits data to data.sqlite.

from sqlite3 import connect

INIT_QUERIES = [
    "CREATE TABLE Calendar (start_time, description)",
    "CREATE TABLE TaskResult (task_file, result)"
]
INIT_QUERY_CHECK = "SELECT name FROM sqlite_master WHERE type = 'table'"
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
    
def init_if_required():
    conn, cur = init_connection()
    if len(cur.execute(INIT_QUERY_CHECK).fetchall()) == 0:
        for query in INIT_QUERIES: cur.execute(query)
    return