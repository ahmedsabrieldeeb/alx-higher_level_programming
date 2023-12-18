#!/usr/bin/python3
"""
    This file has definition of State class that
    maps to states table in mysql database which is
    done throuhg SQLALchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    This class represents the State entity in the MySQL 'states' table.

    Args:
        Base (class): The base class for declarative models in SQLAlchemy.
    """
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",   # could be omitted
                unique=True)

    name = Column(String(128), nullable=False)
