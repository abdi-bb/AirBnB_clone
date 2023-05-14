#!/usr/bin/python3
"""Base Model Unittest Module"""


import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test Base Model"""

    def test_save(self):
        """A method to test the save method"""

        b = BaseModel()
        b.save()

        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
