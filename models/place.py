#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                        Column('place.id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True, nulltable=False),
                        Column('amenity.id', String(60),
                                ForeignKey('amenity.id'),
                                primary_key=True, nulltable=False)
                        ) 


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_t == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nulltable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nulltable=False)
        name = Column(String(128), nulltable=False)
        description = Column(String(1024), nulltable=False)
        number_rooms = Column(Integer, nulltable=False, default=0)
        number_bathrooms = Column(Integer, nulltable=False, default=0)
        max_guest = Column(Integer, nulltable=False, default=0)
        price_by_night = Column(Integer, nulltable=False, default=0)
        latitude = Column(Float, nulltable=True)
        longitude = Column(Float, nulltable=True)
        reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns list of riview instances """
            from models import storage
            all_reviews = storage.all(Review)
            List = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    List.append(review)
            return List

        @property
        def amenities(self):
            """ Returns the list of Amenity instances"""
            from models import storage
            all_amenities = storage.all(Amenity)
            List = []
            for amenities in all_amenities.values():
                if amenities.id in self.amenity_ids:
                    List.append(amenities)
            return List

        @amenities.setter
        def amenities(self, obj):
            """ Adding an amenity.id to amenity.ids"""
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)