# db.py

import oracledb
from config import DB_CONFIG

def get_connection():
    return oracledb.connect(**DB_CONFIG)

def run_query(sql, params=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or {})
            return cursor.fetchall(), [d[0] for d in cursor.description]
