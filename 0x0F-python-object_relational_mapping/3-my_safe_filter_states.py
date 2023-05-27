#!/usr/bin/python3
"""
Lists all the values in the state table that match arg passed
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()

    sql_query = "SELECT * FROM states WHERE name = '{}' \
                 ORDER BY states.id ASC;"
    user_arg = sys.argv[4]
    cur.execute(sql_query, (user_arg,))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
