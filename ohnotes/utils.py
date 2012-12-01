#coding: utf-8

import os
import json
from json import JSONEncoder

from config import project_codename


def read_list(fname, parent_path):
    '''read a list from a file'''
    path = os.path.join(parent_path, fname)
    try:
        return [i.strip() for i in open(path, 'r').readlines()]
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


def import_object(name, arg=None):
    if '.' not in name:
        return __import__(name)
    parts = name.split('.')
    obj = __import__('.'.join(parts[:-1]), None, None, [parts[-1]], 0)
    return getattr(obj, parts[-1], arg)


def register_blueprint(app, blueprint):
    url_prefix = '/%s' % blueprint
    views = import_object('%s.%s.views' % (project_codename, blueprint))
    app.register_blueprint(views.app, url_prefix=url_prefix)
    return app


def register_logger(logger, level, format):
    logger.setLevel(level)
    logger.setFormatter(format)
