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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <statename>"
              .format(sys.argv[0]))
        exit()

    # pool_pre_ping ensures working with non-stale connections
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # extract a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # extract all states in states table referring to its mapped class
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # printing state id fetched from our database if existed
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
