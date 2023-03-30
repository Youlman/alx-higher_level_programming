#!/usr/bin/python3
""" deletes all State objects with a name containing the
letter a from the database"""

import sys
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State).filter(State.name.contains('a'))
    for obj in objs:
        session.delete(obj)
    session.commit()
