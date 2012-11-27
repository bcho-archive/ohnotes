#coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from ohnotes.config import database_url
from ohnotes.models import Base

engine = create_engine(database_url, encoding='utf-8')
db = scoped_session(sessionmaker(bind=engine))


def create_all():
    Base.metadata.create_all(engine)
