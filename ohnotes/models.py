#coding: utf-8

from sqlalchemy import Column, Integer, Unicode
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


#: helper tables
posts_and_words = Table(
    'posts_and_words', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('word_id', Integer, ForeignKey('words.id'))
)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(240), nullable=False)
    words = relationship('Words', secondary=posts_and_words,
                         backref=backref('posts'))

    def __repr__(self):
        return '<Post: %s(%d) with %d word(s)>' % (self.name, self.id,
                                                   len(self.words) or 0)


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(Unicode(240), nullable=False)

    def __repr__(self):
        return '<Word: %s(%d)>' % (self.word, self.id)
