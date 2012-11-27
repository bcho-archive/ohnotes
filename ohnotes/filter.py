#coding: utf-8

from jieba import cut

from ohnotes.config import data_dir
from .utils import read_list


ignorewords = read_list('ignorewords.list', data_dir) or ['\n']
stopwords = read_list('stopwords.list', data_dir)


def filter(raw_buffer):
    #: clean the raw text
    for w in ignorewords:
        raw_buffer = ' '.join(raw_buffer.split(w))
    #: tokenize the text
    words = cut(raw_buffer)
    #: remove useless and repeated words
    ret = []
    for w in words:
        if w.lower() not in ret + ignorewords + stopwords:
            ret.append(w.lower())
    return ret
