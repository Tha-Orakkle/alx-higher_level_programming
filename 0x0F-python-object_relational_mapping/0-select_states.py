#!/usr/bin/python3
"""
Lists all states in the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

id __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
