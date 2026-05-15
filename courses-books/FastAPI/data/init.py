"""Initialize SQLite database"""

import os
from sqlite3 import connect, Connection, Cursor, IntegrityError


conn: Connection | None = None
curs: Cursor | None = None


def get_db(name: str|None = None, reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs

    if conn:
        if not reset:
            return
        conn = None

    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB")

    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()


get_db()


if __name__ == "__main__":
    curs.execute("""
        CREATE TABLE IF NOT EXISTS creature(
            name UNIQUE,
            description,
            country,
            area,
            aka
        )
    """)

    
    curs.execute("""
        CREATE TABLE IF NOT EXISTS explorer(
                name TEXT PRIMARY KEY,
                country TEXT,
                description TEXT
        )
    """)



    curs.execute("""
        CREATE TABLE IF NOT EXISTS user(
            name TEXT PRIMARY KEY,
            hash TEXT
        )
    """)


    curs.execute("""
        CREATE TABLE IF NOT EXISTS xuser(
            name TEXT PRIMARY KEY,
            hash TEXT
        )
    """)

