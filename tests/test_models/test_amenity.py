#!/usr/bin/python3
"""
Test for State class
"""


import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTest(unittest.TestCase):
    """A Class to Test the Amenity class"""

    def test_attr(self):
        """Test if attributes exist"""

        a = Amenity()
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'name'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the Amenity class attributes"""

        a = Amenity()
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.name, str)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_class_exist(self):
        """Test if the Amenity Class Exists"""

        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")


if __name__ == '__main__':
    unittest.main()
