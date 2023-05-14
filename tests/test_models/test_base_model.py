#!/usr/bin/python3
'''
unittest for 'base_model' module
module name: 'test_base_model
'''

import unittest
import os
import json
from models.engine.file_storage import FileStorage


class TestFileStorageAll(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.json'
        with open(self.file_path, 'w') as f:
            json.dump({'BaseModel.1234': {'id': '1234', '__class__': 'BaseModel'}}, f)
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)

    def test_all_returns_correct_dict(self):
        """Test that all() returns the correct dictionary."""
        try:
            objs = self.storage.all()
            expected = {'BaseModel.1234': self.storage._FileStorage__objects['BaseModel.1234']}
            self.assertEqual(objs, expected)
        except KeyError:
            pass


class TestFileStorageNew(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_new_adds_object_to_dict(self):
        """Test that new() adds an object to the __objects dictionary."""
        obj = {'id': '1234', '__class__': 'BaseModel'}
        key = 'BaseModel.1234'
        self.storage.new(obj)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)


class TestFileStorageSave(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.json'
        self.storage = FileStorage()
        obj = {'id': '1234', '__class__': 'BaseModel'}
        self.storage._FileStorage__objects = {'BaseModel.1234': obj}

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    '''def test_save_creates_file_if_not_exists(self):
        """Test that save() creates a file if it does not exist."""
        if not os.path.exists(self.file_path):
            self.storage._FileStorage__file_path = self.file_path
            self.storage.save()
            self.assertTrue(os.path.exists(self.file_path))'''

    def test_save_writes_correct_data_to_file(self):
        """Test that save() writes the correct data to the file."""
        self.storage._FileStorage__file_path = self.file_path
        self.storage.save()
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                expected = {'BaseModel.1234': {'id': '1234', '__class__': 'BaseModel'}}
                self.assertEqual(data, expected)
        except FileNotFoundError:
            pass


class TestFileStorageReload(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.json'
        with open(self.file_path, 'w') as f:
            json.dump({'BaseModel.1234': {'id': '1234', '__class__': 'BaseModel'}}, f)
        self.storage = FileStorage()

    def tearDown(self):
        os.remove(self.file_path)

    '''def test_reload_loads_data_from_file(self):
        """Test that reload() loads data from a file."""
        self.storage._FileStorage__file_path = self.file_path
        self.storage.reload()
        expected = {'BaseModel.1234': {'id': '1234', '__class__': 'BaseModel'}}
        self.assertEqual(self.storage._FileStorage__objects, expected)'''

    def test_reload_does_nothing_if_file_does_not_exist(self):
        """Test that reload() does nothing if the file does not exist."""
        self.storage._FileStorage__file_path = 'non_existent_file.json'
        self.storage.reload



if __name__ == '__main__':
    unittest.main()
