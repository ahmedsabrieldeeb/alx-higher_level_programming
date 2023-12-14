#!/usr/bin/python3
"""
    Connecting to mysql-server fetching some data from database "hbtn_0e_0_usa"
"""

import sys
import MySQLdb


def main():
    """main program"""

    # check the proper usage of module
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        exit()

    # fetching the credentials from the input arguments
    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()

    # write here the QUERY
    sql_query = "SELECT * FROM states ORDER BY id"

    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # displaying the resuts
    for row in rows:
        print(row)

    # closing everything before leaving
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
