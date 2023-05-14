#!/usr/bin/python3
'''
module: file_storage
class: FileStorage
'''

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''class FileStorage'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns dict __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''assigns obj to __objects at key <obj class name>.id'''
        tmp = None
        if obj != tmp:
            key = f'{obj.__class__.__name__}.{obj.id}'
            FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to json'''
        obj_dict = {}
        for k, obj in FileStorage.__objects.items():
            obj_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        '''deserializes the json back to __objects'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    value['__class__'] = class_name
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except (ValueError, FileNotFoundError):
            pass
