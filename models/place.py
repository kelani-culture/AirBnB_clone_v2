#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity',
                        Base.metadata,
                        Column('place_id', String(60), ForeignKey('places.id'),
                                primary_key=True, nullable=False),
                        Column('amenities_id', String(60), ForeignKey('amenities.id'),
                                primary_key=True, nullable=False)
                        )

class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False) 
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        place = relationship("Review", backref='place', cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                       back_populates='place_amenities', viewonly=False)

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
    def amenities(self):
        from models.__init__ import storage
        from models.amenity import Amenity
        amenities = storage.all(Amenity)
        place_amenitiesList = []
        for amenity in amenities:
            if amenity.id == self.id:
                place_amenitiesList.append(amenity)
        Place.amenities = place_amenitiesList
        return place_amenitiesList

    @amenities.setter
    def amenities(self, obj):
        from models.__init__ import storage
        from models.amenity import Amenity
        
        if isinstance(obj, Amenity):
            self.amenities_ids.append(obj.id)