#!/usr/bin/python3
'''
module city
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''class City'''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        '''Constructor'''
        super().__init__(*args, **kwargs)
