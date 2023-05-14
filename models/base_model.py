#!/usr/bin/python3
"""
A Base Model Module
"""


from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """A Parent Base Model Class"""

    def __init__(self, *args, **kwargs):
        """A Method that initializes
        everytime object is created
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            a = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, a)
                    setattr(self, key, value)

    def __str__(self):
        """A Method to return a dictionary
        attribute
        """

        class_name = "[{}] ".format(self.__class__.__name__)
        class_id = "({}) ".format(self.id)
        class_dict = "{}".format(self.__dict__)
        return class_name + class_id + class_dict

    def save(self):
        """A Method that updates the updated
        at attribute
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A Method that return a dictionary
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        if hasattr(self, 'created_at'):
            my_dict['created_at'] = self.created_at.isoformat()
        if hasattr(self, 'updated_at'):
            my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict.pop('_sa_instance_state', None)
        return my_dict
