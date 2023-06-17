#!/usr/bin/python3
"""
Contains the class `State` and Base, an instance of declarative_base()
"""

from sqlalchemy import COlumn, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """Class with id and attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
