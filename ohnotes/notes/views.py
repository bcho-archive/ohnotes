#coding: utf-8

from flask import Blueprint, jsonify, abort

from ohnotes import worker

app = Blueprint('notes', __name__)


@app.route('/<int:post_id>', methods=['GET'])
def load_post(post_id):
    content = worker.load_post(post_id)
    if content:
        return jsonify(id=post_id, content=content)
    abort(404)


@app.route('', methods=['GET'])
def load_posts():
    posts = [{'id': i.id, 'name': i.name} for i in worker.load_posts()]
    if posts:
        return jsonify(posts=posts)
    abort(404)
