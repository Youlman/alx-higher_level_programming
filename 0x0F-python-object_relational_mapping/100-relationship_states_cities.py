#!/usr/bin/python3
"""that creates the State “California” with the City “San Francisco” 
from the database"""

import sys
from relationship_city import City 
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    c = City(name="San Francisco")
    s = State(name="California", cities=[c])
    session.add(s)
    session.add(c)
    session.commit()