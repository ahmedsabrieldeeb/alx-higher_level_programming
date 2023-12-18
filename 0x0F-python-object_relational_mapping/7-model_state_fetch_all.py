#!/usr/bin/python3
"""
    a script to fetach all data coming from a table
    in mysql database
"""

import sys
from model_state import Base, State

from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)


def main():
    """ main program """

    # check the proper usage of module
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        exit()

    # mysql_db = {
    #     'service_name': 'mysql',
    #     'username': sys.argv[1],
    #     'password': sys.argv[2],
    #     'database': sys.argv[3],
    #     'host': 'localhost',
    #     'port': 3306
    # }
    # url = URL(**mysql_db, query=dict(service_name='mysql'))

    # pool_pre_ping ensures working with non-stale connections
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # extract a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # extract all states in states table referring to its mapped class
    states = session.query(State).all()

    # printing names of states fetched from our database
    for i in range(len(states)):
        print(f"{i+1}: {states[i].name}")


if __name__ == "__main__":
    main()
