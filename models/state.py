#!/usr/bin/python3
'''
module state
'''

from models.base_model import BaseModel


class State(BaseModel):
    '''class State'''
    name = ''

    def __init__(self, *args, **kwargs):
        '''Instantiation of class State'''
        super().__init__(*args, **kwargs)
