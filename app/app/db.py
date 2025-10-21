import os
import psycopg2
from contextlib import contextmanager

DATABASE_URL = os.environ["DATABASE_URL"]

@contextmanager
def get_conn():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()

def ping():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("select now()")
            (now,) = cur.fetchone()
            return {"ok": True, "db_time": now.isoformat()}
