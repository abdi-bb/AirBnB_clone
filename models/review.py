#!/usr/bin/python3
'''
module review
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''class Review'''
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        '''Constructor'''
        super().__init__(*args, **kwargs)
