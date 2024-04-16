#!/usr/bin/python3
""" Script defines "Amenity "class based on the storage type specified in the environment variable """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ amenity class inherits from basemodel and base and storage type is set to 'db' if not then 'tablename' is simply an empty string """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes an instance of amenity class, calls the parent class 'basemodel' with any provided *args and *kwargs"""
        super().__init__(*args, **kwargs)
