#!/usr/bin/env python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

storage_type = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        cities = relationship('Place', backref='cities', cascade='all, delete-orphan')
    
    else:
        state_id = ""
        name = ""
