#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
 
    else:
        place_id = ""
        user_id = ""
        text = ""
    
    @property
    def reviews(self):
        from models.__init__ import storage
        from models.place import Place
        reviewed_placeList = []
        place_lst = storage.all(Place)
        for place in place_lst:
            if place.id == self.id:
                reviewed_placeList.append(place)
        return reviewed_placeList