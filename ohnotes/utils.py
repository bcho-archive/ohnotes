#coding: utf-8

import os
import json
from json import JSONEncoder


def read_list(fname, parent_path):
    '''read a list from a file'''
    path = os.path.join(parent_path, fname)
    try:
        return [unicode(i.strip()) for i in open(path, 'r').readlines()]
    #: always return a list
    except:
        return []


def _json(func):
    '''JSON wrapper'''
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs), cls=Dict)
    return wrapper


class Dict(JSONEncoder):
    '''Dict for serializing a obj.
    
    :property __keys__: Keys will be contained in the dict.
    '''
    __keys__ = []

    @property
    def dict(self):
        r = {}
        for key in self.__keys__:
            r[key] = self.__dict__.get(key, None)
        return r

    def default(self, o):
        '''For JSON encoding'''
        if isinstance(o, Dict):
            return o.dict
        return super(JSONEncoder, self).default(o)
