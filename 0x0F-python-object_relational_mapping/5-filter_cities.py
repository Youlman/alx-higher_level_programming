#!/usr/bin/python3
"""script that lists all states where name matches  an argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], 
        passwd=sys.argv[2],                         
        db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities AS c \
                        INNER JOIN states AS s \
                            ON c.state_id = s.id \
                        ORDER BY c.id;")
    print(",".join([row for row in cur.fetchall()
                    if row[4] == sys.argv[4]]))
    cur.close()
    conn.close()
