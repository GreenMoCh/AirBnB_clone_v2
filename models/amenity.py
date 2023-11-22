#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Amenity Class """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nulltable=False)
    else:
        name = ""
