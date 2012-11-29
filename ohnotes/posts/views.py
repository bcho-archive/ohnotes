#coding: utf-8

from flask import Blueprint, jsonify, abort

from ohnotes import worker

app = Blueprint('posts', __name__)


@app.route('/<int:post_id>', methods=['GET'])
def load_post(post_id):
    content = worker.load_post(post_id)
    if content:
        return jsonify(content=content)
    abort(404)
