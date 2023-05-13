#!/usr/bin/python3
"""
A Base Model Module
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """A Parent Base Model Class"""

    def __init__(self, *args, **kwargs):
        """A Method that initializes
        everytime object is created
        """

        if not kwargs:
            self.name = "Danny"
            sef.my_number = '2023'
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
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

    def to_dict(self):
        """A Method that turns an object
        to a dictionary
        """

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
