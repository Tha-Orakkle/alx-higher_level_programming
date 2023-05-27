#!/usr/bin/python3
"""
Lists all states where name matches argument passed
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
    WHERE name COLLATE Latin1_General_CS_AS = '{}' \
    ORDER BY states.id ASC;".format(sys.argv[4]))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
