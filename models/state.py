#!/usr/bin/env python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')
class State(BaseModel, Base):
    """ State class """

    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        state = relationship('City', backref='state', cascade='all, delete-orphan')

    #Filestorage
    else:
        name = ""
        @property
        def cities(self):
            #TODO: set a getter attribute that returns a list of cities instance
            # state_id
            return self