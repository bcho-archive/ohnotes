#coding: utf-8

from flask import Blueprint, json, abort, Response

from ohnotes import worker
from ohnotes.utils import Dict

app = Blueprint('query', __name__)


@app.route('/word/<string:word>', methods=['GET'])
def query_word(word):
    ret = worker.query(word)
    if ret:
        return Response(json.dumps(ret, cls=Dict), mimetype='application/json')
    abort(404)
