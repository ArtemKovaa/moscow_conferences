import sqlite3

from .setup_db import db_name


def execute_query(query, params=None):
    result = None
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("BEGIN TRANSACTION")

    try:
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)

        if query.find("SELECT") >= 0:
            result = cur.fetchall()

        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        raise e

    conn.commit()
    conn.close()
    return result
