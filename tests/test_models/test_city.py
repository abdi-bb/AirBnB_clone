#!/usr/bin/python3
"""
Test for City class
"""


import unittest
from models.city import City
from datetime import datetime


class CityTest(unittest.TestCase):
    """A Class to Test the City class"""

    def test_attr(self):
        """Test if attributes exist"""

        c = City()
        self.assertTrue(hasattr(c, 'id'))
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(hasattr(c, 'created_at'))
        self.assertTrue(hasattr(c, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the City class attributes"""

        c = City()
        self.assertIsInstance(c.id, str)
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)
        self.assertIsInstance(c.created_at, datetime)
        self.assertIsInstance(c.updated_at, datetime)

    def test_class_exist(self):
        """Test if the City Class Exists"""

        c = City()
        self.assertEqual(str(type(c)), "<class 'models.city.City'>")


if __name__ == '__main__':
    unittest.main()
