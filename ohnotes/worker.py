#coding: utf-8

'''
    worker
    ~~~~~~

    Do every dirty job.
'''

import os

from ohnotes.db import db
from ohnotes.models import Post, Word


def _get(model, condition):
    r = db.query(model).filter(condition)
    return r.one() if r.count() else None


def get_word(word):
    return _get(Word, (Word.word == word))


def get_post(postpath):
    return _get(Post, (Post.path == postpath))


def parse_post(fname, path):
    '''Parse a post and store its words.
    
    :param fname: The name of the post.

    :param path: The absolute path of the post.
    '''
    from ohnotes.filter import filter

    raw_buffer = open(path, 'r').read()
    words = filter(raw_buffer)
    
    p = get_post(path) or Post(fname, path)
    for w in words:
        w = get_word(w) or Word(w)
        db.add(w)
        p.words.append(w)
    db.add(w)
    db.commit()


def parse_posts(path):
    '''Parse all posts under the gave path.
    
    :param path: The absolute parent path of the posts.
    '''
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.splitext(f)[0].decode('utf-8')
            fullpath = os.path.join(dirpath, f).decode('utf-8')
            parse_post(fname, fullpath)
