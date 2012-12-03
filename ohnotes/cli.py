#!/usr/bin/env python
#coding: utf-8

import sys
from docopt import docopt

import ohnotes
from ohnotes import worker, server, config


documentation = {}
documentation['help'] = '''%(name)s v%(version)s

Usage:
    %(name)s update [-p <path>|--path=<path>]
    %(name)s server [-p <port>|--port=<port>]
    %(name)s -h | --help
    %(name)s --version
''' % {
    'name': config.project_codename,
    'version': ohnotes.__version__,
}

documentation['update'] = '''
Usage:
    %(name)s update [-p <path>|--path=<path>]

Options:
    -h --help           show this message.
    -p --path=<path>    specify a path where are your notes in.
''' % {
    'name': config.project_codename
}

documentation['server'] = '''
Usage:
    %(name)s server [-p <port>|--port=<port>]

Options:
    -h --help           show this message.
    -p --port=<port>    specify the server port.
''' % {
    'name': config.project_codename
}


def _parse_path(path=None):
    path = config.notes_path if not path else path
    worker.parse_notes(path)


def _main():
    command = 'help'
    if len(sys.argv) > 1:
        command = sys.argv[1]

    if command in documentation:
        args = docopt(documentation[command])
    #: create the args manually
    else:
        args = docopt(
            documentation['help'],
            version='%s v%s' % (config.project_codename, ohnotes.__version__)
        )

    arg_port = args.get('--port') or 8000
    arg_path = args.get('--path') or config.notes_path

    if command == 'update':
        _parse_path(arg_path)
    elif command == 'server':
        server.run(port=int(arg_port))


if __name__ == '__main__':
    _main()
