#coding: utf-8

from flask import Flask, jsonify

from utils import register_blueprint
from config import blueprints


#: init app
app = Flask(__name__)
app.config.from_pyfile('config.py')


#: register blueprints
for blueprint in blueprints:
    register_blueprint(app, blueprint)


@app.errorhandler(404)
def not_found(error):
    return jsonify(message='Not found.'), 404
