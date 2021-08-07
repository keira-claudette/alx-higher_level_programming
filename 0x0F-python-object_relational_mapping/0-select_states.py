#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa.

1. Establish a connection to mysql server and select database
2. Query the database
3. List results

"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id LIMIT 5"

    cursor.execute(sql)

    result = cursor.fetchall()

    for item in result:
        print(item)

    cursor.close()
    db.close()


#if __name__ == "__main__"
# Python only runs this script if file is run directly ,not called via import.
