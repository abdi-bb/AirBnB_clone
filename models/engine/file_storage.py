#!/usr/bin/python3
'''
module: file_storage
class: FileStorage
'''

import json
from models.base_model import BaseModel


class FileStorage():
    '''class FileStorage'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns dict __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''assigns obj to __objects at key <obj class name>.id'''
        if obj is None:
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
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    value['__class__'] = class_name
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except Exception:
            pass
