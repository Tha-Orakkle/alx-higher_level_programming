#!/usr/bin/python3
"""
Lists all cities in the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
    FROM cities c JOIN states s ON c.state_id = s.id;")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
