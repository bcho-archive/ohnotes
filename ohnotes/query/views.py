#coding: utf-8

from flask import Blueprint, json, jsonify, abort, Response

from ohnotes import worker
from ohnotes.utils import Dict

app = Blueprint('query', __name__)


@app.route('/word/<string:word>', methods=['GET'])
def query_word(word):
    ret = worker.query(word)
    if ret:
        return Response(json.dumps(ret, cls=Dict), mimetype='application/json')
    abort(404)


@app.route('/post/<int:post_id>', methods=['GET'])
def load_post(post_id):
    content = worker.load_post(post_id)
    if content:
        return jsonify(content=content)
    abort(404)
