#coding: utf-8

from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from .utils import Dict


Base = declarative_base()


#: helper tables
notes_and_words = Table(
    'notes_and_words', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('word_id', Integer, ForeignKey('words.id'))
)


class Note(Base, Dict):
    __tablename__ = 'notes'
    __keys__ = ['id', 'name', 'path']

    id = Column(Integer, primary_key=True)
    name = Column(String(240), nullable=False)
    path = Column(String(500), nullable=False, unique=True)
    words = relationship('Word', secondary=notes_and_words,
                         backref=backref('notes'))

    def __init__(self, notename, path):
        self.name = notename
        self.path = path

    def __repr__(self):
        return '<Note: %s(%d) with %d word(s)>' % (self.name.encode('utf-8'),
                self.id, len(self.words) or 0)


class Word(Base, Dict):
    __tablename__ = 'words'
    __keys__ = ['id', 'word']

    id = Column(Integer, primary_key=True)
    word = Column(String(240), nullable=False)

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return '<Word: %s(%d)>' % (self.word, self.id)
