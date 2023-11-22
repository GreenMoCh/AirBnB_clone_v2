#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if storage_t == 'db':
        email = Column(String(128), nulltable=False)
        password = Column(String(128), nulltable=False)
        first_name = Column(String(128), nulltable=True)
        last_name = Column(String(128), nulltable=True)
        places = relationship('Place', backref='user', cascade='all, delete, delete-orhphan')
        reviews = relationship('Review', backref='user', cacade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
