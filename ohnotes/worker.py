#coding: utf-8

'''
    worker
    ~~~~~~

    Do every dirty job.
'''

import os

from ohnotes.base import logger
from ohnotes.db import db
from ohnotes.models import Note, Word


def _get_one(model, condition):
    r = db.query(model).filter(condition)
    return r.one() if r.count() else None


def _get(model, condition=None):
    r = db.query(model).filter(condition)
    return r.all() if r.count() else None


def get_word(word):
    return _get_one(Word, (Word.word == word))


def get_note(notepath):
    return _get_one(Note, (Note.path == notepath))


def parse_note(fname, path):
    '''Parse a note and store its words.
    
    :param fname: The name of the note.

    :param path: The absolute path of the note.
    '''
    from ohnotes.filter import filter

    raw_buffer = load_local_note(path)
    words = filter(raw_buffer)
    
    p = get_note(path) or Note(fname, path)
    for w in words:
        w = get_word(w) or Word(w)
        db.add(w)
        p.words.append(w)
    db.add(w)
    db.commit()


def parse_notes(path):
    '''Parse all notes under the gave path.
    
    :param path: The absolute parent path of the notes.
    '''
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.splitext(f)[0].decode('utf-8')
            fullpath = os.path.join(dirpath, f).decode('utf-8')
            logger.debug('parsing %s(%s)' % (fname, fullpath))
            parse_note(fname, fullpath)


def query(word):
    '''Search some notes basic on a word.'''
    if not isinstance(word, unicode):
        word = word.decode('utf-8')
    words = _get(Word, (Word.word.like('%' + word + '%')))
    if words:
        ret = [p for w in words for p in w.notes]
        return list(set(ret))
    else:
        return None


def load_local_note(path):
    '''Load a local note.
    
    :param path: The **absolute** path of the file.
    '''
    if not os.path.isfile(path):
        return None
    return open(path).read().decode('utf-8')


# TODO load database note
def load_db_note(note):
    '''Load a note from db.
    
    :param note: A `Note` instance.
    '''
    return None


def load_note(note_id):
    '''Load a note.

    :param note_id: The id of the note.
    '''
    note = _get_one(Note, (Note.id == note_id))
    # TODO load database note
    if note and note.path:
        return load_local_note(note.path)
    return None


def load_notes():
    '''Load all notes.'''
    return _get(Note)
