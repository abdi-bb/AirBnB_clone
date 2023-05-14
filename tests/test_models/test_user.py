#!/usr/bin/python3
"""
Test for User class
"""


import unittest
from models.user import User
from datetime import datetime


class UserTest(unittest.TestCase):
    """A Class to Test the User class"""

    def test_attr(self):
        """Test if attributes exist"""

        u = User()
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(hasattr(u, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the attributes"""

        u = User()
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)

    def test_class_exist(self):
        """Test if the Class Exists"""

        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")


if __name__ == '__main__':
    unittest.main()
