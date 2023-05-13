#!/usr/bin/python3
'''
module amenity
'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class Amenity'''
    name = ''

    def __init__(self, *args, **kwargs):
        '''Constructor'''
        super().__init__(*args, **kwargs)
