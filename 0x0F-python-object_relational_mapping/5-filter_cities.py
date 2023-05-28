#!/usr/bin/python3
"""
Lists all cities of a state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()

    sql_query = "SELECT c.name FROM cities c \
                 JOIN states s ON c.state_id = s.id \
                 WHERE s.name = %s;"
    user_arg = sys.argv[4]
    cur.execute(sql_query, (user_arg,))
    cities = cur.fetchall()

    print(", ".join(city for city in cities))
    cur.close()
    db.close()
