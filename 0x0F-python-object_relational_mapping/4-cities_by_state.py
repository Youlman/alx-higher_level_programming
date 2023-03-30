#!/usr/bin/python3
"""script that lists all states where name matches  an argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.`id`, c.`name`, s.`name` FROM `cities` AS c \
                        INNER JOIN `states` AS s \
                            ON c.`state_id` = s.`id` \
                        ORDER BY c.`id`;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
