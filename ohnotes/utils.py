#coding: utf-8

import os


def read_list(fname, parent_path):
    '''read a list from a file'''
    path = os.path.join(parent_path, fname)
    try:
        return [i.strip() for i in open(path, 'r').readlines()]
    #: always return a list
    except:
        return []
