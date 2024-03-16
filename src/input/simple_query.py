"""Simple query for testing purposes"""

import sqlite3

from common import get_database_path


def simple_query():
    """Simple query for testing purposes"""
    query = "SELECT * FROM house_prices LIMIT 5"
    conn = sqlite3.connect(get_database_path())
    result = conn.execute(query).fetchall()
    conn.close()
    for t in result:
        print(t)


if __name__ == "__main__":
    simple_query()