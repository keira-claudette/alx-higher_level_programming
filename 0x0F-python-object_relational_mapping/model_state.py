#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
This file contains  the class definition of a State and an instance
 Base = declarative_base():
 Links to MySQL table States.
"""

Base = declarative_base()


class State(Base):
    """ Defines class State, an object representation of table states
    from database hbtn_0e_6_usa.
    class attributes:
                     id = column id from table states
                     name = column name from table states
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
