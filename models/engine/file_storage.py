#!/usr/bin/python3
'''
module: file_storage
class: FileStorage
'''

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    '''class FileStorage'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for k, obj in FileStorage.__objects.items():
            obj_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
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
