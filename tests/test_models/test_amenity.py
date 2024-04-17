#!/usr/bin/python3
"""Script to test the Amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os

class test_Amenity(test_basemodel):
    """This class inherits from test_basemodel class """

    def __init__(self, *args, **kwargs):
        """The constructor ('__init__') of tets_amenity calls the superclass constructor """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """the test cases """
        new = self.value()
        self.assertEqual(type(new.name), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))
