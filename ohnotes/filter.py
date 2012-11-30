#coding: utf-8

'''
    filter
    ~~~~~~

    Split the post into a keywords set.
'''

from jieba import cut

from ohnotes.config import data_dir
from .utils import read_list


builtin_ignore = '\n \t'.split(' ')
ignorewords = set(read_list('ignorewords.list', data_dir) + builtin_ignore)
stopwords = set(read_list('stopwords.list', data_dir))


# TODO use built-in `filter` instead?
def filter(raw_buffer):
    #: clean the raw text
    for w in ignorewords:
        raw_buffer = ' '.join(raw_buffer.split(w))
    #: tokenize the text
    words = cut(raw_buffer)
    #: remove useless and repeated words
    ret = []
    ignored = ignorewords.union(stopwords)
    for w in words:
        w = w.strip().lower()
        if w not in ret and w not in ignored:
            ret.append(w)
    return ret
