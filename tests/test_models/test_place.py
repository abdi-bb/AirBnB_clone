#!/usr/bin/python3
"""
Test for Place class
"""


import unittest
from models.place import Place
from datetime import datetime


class PlaceTest(unittest.TestCase):
    """A Class to Test the Place class"""

    def test_attr(self):
        """Test if attributes exist"""

        p = Place()
        self.assertTrue(hasattr(p, 'id'))
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertTrue(hasattr(p, 'user_id'))
        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'description'))
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertTrue(hasattr(p, 'created_at'))
        self.assertTrue(hasattr(p, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the place attributes"""

        p = Place()
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)
        self.assertIsInstance(p.created_at, datetime)
        self.assertIsInstance(p.updated_at, datetime)

    def test_class_exist(self):
        """Test if the Place Class Exists"""

        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")


if __name__ == '__main__':
    unittest.main()
