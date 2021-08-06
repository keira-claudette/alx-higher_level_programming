#!/usr/bin/python3

import sys
import MySQLdb

"""
A script that takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.

"""


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name REGEXP '^N'"

    cursor.execute(sql)

    result = cursor.fetchall()

    for item in result:
        print(item)
