#coding: utf-8

def run(port):
    from ohnotes.app import app

    #: also make the server global visitable
    app.run(host='0.0.0.0', port=port)
