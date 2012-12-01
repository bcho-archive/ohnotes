#coding: utf-8

from flask import Blueprint, jsonify, abort

from ohnotes import worker

app = Blueprint('notes', __name__)


@app.route('/<int:note_id>', methods=['GET'])
def load_note(note_id):
    content = worker.load_note(note_id)
    if content:
        return jsonify(id=note_id, content=content)
    abort(404)


@app.route('', methods=['GET'])
def load_notes():
    notes = worker.load_notes()
    if notes:
        return jsonify(notes=[{'name': i.name, 'id': i.id} for i in notes])
    abort(404)
