#coding: utf-8

import os


#: basic config
project_codename = 'ohnotes'
DEBUG = True

#: path settings
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(parent_dir, 'data')
db_file_name = '%s%s.sqlite' % (project_codename,
                                '_dev' if DEBUG else '')

#: database settings
database_path = os.path.join(data_dir, db_file_name)
database_url = 'sqlite:///%s' % (database_path)

#: enabled blueprints
blueprints = ['query', 'posts']
