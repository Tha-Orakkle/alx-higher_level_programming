#!/usr/bin/python3
"""
lists all the City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchmey.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id)

    for row in result:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
