#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage_t
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_t == 'db':
        name = Column(String(128), nulltable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nulltable=False)
        places = relationship('Place', backref=cities, cascade='all, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
