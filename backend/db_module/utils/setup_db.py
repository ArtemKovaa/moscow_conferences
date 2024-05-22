import sqlite3

db_name = 'db.sqlite3'
migrate_schema_query = """
        CREATE TABLE IF NOT EXISTS conferences
        (
            id CHAR(32) PRIMARY KEY,
            name VARCHAR(50) NOT NULL UNIQUE,
            description VARCHAR(500),
            start_date TEXT NOT NULL,
            location VARCHAR(100) NOT NULL
        )
"""


def init_schema(directory):
    conn = sqlite3.connect(directory.__str__() + "/" + db_name)
    cur = conn.cursor()

    cur.execute(migrate_schema_query)

    conn.commit()
    conn.close()
