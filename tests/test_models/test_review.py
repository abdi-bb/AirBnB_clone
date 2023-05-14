#!/usr/bin/python3
"""
Test for Review class
"""


import unittest
from models.review import Review
from datetime import datetime


class ReviewTest(unittest.TestCase):
    """A Class to Test the Review class"""

    def test_attr(self):
        """Test if attributes exist"""

        r = Review()
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))
        self.assertTrue(hasattr(r, 'created_at'))
        self.assertTrue(hasattr(r, 'updated_at'))

    def test_attr_types(self):
        """Test the Types of the Review class attributes"""

        r = Review()
        self.assertIsInstance(r.id, str)
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)
        self.assertIsInstance(r.created_at, datetime)
        self.assertIsInstance(r.updated_at, datetime)

    def test_class_exist(self):
        """Test if the Review Class Exists"""

        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")


if __name__ == '__main__':
    unittest.main()
