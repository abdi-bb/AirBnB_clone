#!/usr/bin/python3
"""
Test for State class
"""


import unittest
from models.state import State
from datetime import datetime


class StateTest(unittest.TestCase):
    """A Class to Test the State class"""

    def test_attr(self):
        """Test if attributes exist"""

        s = State()
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'name'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the state attributes"""

        s = State()
        self.assertIsInstance(s.id, str)
        self.assertIsInstance(s.name, str)
        self.assertIsInstance(s.created_at, datetime)
        self.assertIsInstance(s.updated_at, datetime)

    def test_class_exist(self):
        """Test if the State Class Exists"""

        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")


if __name__ == '__main__':
    unittest.main()
