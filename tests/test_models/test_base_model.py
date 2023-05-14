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


class TestBaseModelInit(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()

    def test_has_id_attr(self):
        self.assertTrue(hasattr(self.bm, 'id'))

    def test_has_created_at_attr(self):
        self.assertTrue(hasattr(self.bm, 'created_at'))

    def test_has_updated_at_attr(self):
        self.assertTrue(hasattr(self.bm, 'updated_at'))

    def test_id_is_str(self):
        self.assertIsInstance(self.bm.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_id_is_unique(self):
        bm2 = BaseModel()
        self.assertNotEqual(self.bm.id, bm2.id)


class TestBaseModelSave(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()

    def test_save_updates_updated_at(self):
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(self.bm.updated_at, old_updated_at)


class TestBaseModelToDict(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()

    def test_to_dict_returns_dict(self):
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict, dict)

    def test_to_dict_has_expected_keys(self):
        bm_dict = self.bm.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertTrue(key in bm_dict)

    def test_to_dict_has_expected_types(self):
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict['__class__'], str)
        self.assertIsInstance(bm_dict['id'], str)
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

    def test_to_dict_has_expected_values(self):
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['id'], self.bm.id)
        self.assertEqual(bm_dict['created_at'], self.bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], self.bm.updated_at.isoformat())


class TestBaseModelStr(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()

    def test_str_returns_str(self):
        bm_str = str(self.bm)
        self.assertIsInstance(bm_str, str)


if __name__ == '__main__':
    unittest.main()
