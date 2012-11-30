#coding: utf-8

'''
    worker
    ~~~~~~

    Do every dirty job.
'''

import os

from ohnotes.db import db
from ohnotes.models import Post, Word


def _get_one(model, condition):
    r = db.query(model).filter(condition)
    return r.one() if r.count() else None


def _get(model, condition=None):
    r = db.query(model).filter(condition)
    return r.all() if r.count() else None


def get_word(word):
    return _get_one(Word, (Word.word == word))


def get_post(postpath):
    return _get_one(Post, (Post.path == postpath))


def parse_post(fname, path):
    '''Parse a post and store its words.
    
    :param fname: The name of the post.

    :param path: The absolute path of the post.
    '''
    from ohnotes.filter import filter

    raw_buffer = load_local_post(path)
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


def query(word):
    '''Search some posts basic on a word.'''
    if not isinstance(word, unicode):
        word = word.decode('utf-8')
    words = _get(Word, (Word.word.like('%' + word + '%')))
    if words:
        ret = [p for w in words for p in w.posts]
        return list(set(ret))
    else:
        return None


def load_local_post(path):
    '''Load a local post.
    
    :param path: The **absolute** path of the file.
    '''
    if not os.path.isfile(path):
        return None
    return open(path).read().decode('utf-8')


# TODO load database post
def load_db_post(post):
    '''Load a post from db.
    
    :param post: A `Post` instance.
    '''
    return None


def load_post(post_id):
    '''Load a post.

    :param post_id: The id of the post.
    '''
    post = _get_one(Post, (Post.id == post_id))
    # TODO load database post
    if post and post.path:
        return load_local_post(post.path)
    return None
