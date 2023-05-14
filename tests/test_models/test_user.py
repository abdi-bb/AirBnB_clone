#!/usr/bin/python3
"""
Test for User class
"""


import unitttest
from models.user import User
from datetime import datetime


class UserTest(unittest.TestCase):
    """A Class to Test the User class"""

    def test_attr(self):
        """Test if attributes exist"""

        u = User()
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the attributes"""

        u = User()
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(slef.u.password, str)
        self.assertIsInstance(self.u.created_at, datetime)
        self.assertIsInstance(self.u.updated_at, datetime)

    def test_class_exist(self):
        """Test if the Class Exists"""

        u = User()
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")
