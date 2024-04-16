#!/usr/bin/python3
""" This script defines a class 'City' """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class City(BaseModel, Base):
    """ The city class attributes """
    if getenv('HBNB_TYPE_STORAGE') = 'db':
        __tablename__  = 'cities'
        name = Column(String(128),
                nullable=False)
        state_id = Column(String(60),
                ForeighnKey('ststes.id'),
                nullable=False)
        places = relationship("Place",
                backref="cities",
                cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """ Initializes city """
        super().__init__(*args, **kwargs)
