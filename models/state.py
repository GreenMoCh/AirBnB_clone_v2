#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nulltable=False)
    cities = relationship("City", cascase='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        List = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                List.append(var[key])
        for elem in List:
            if (elem.state_id == self.id):
                result.append(elem)
        return result
