#coding: utf-8

from flask import Flask, jsonify

from ohnotes.base import logger
from .utils import register_blueprint, register_logger
from ohnotes.config import blueprints


#: init app
app = Flask(__name__)
app.config.from_pyfile('config.py')


#: register blueprints
for blueprint in blueprints:
    logger.info('registering %s' % (blueprint))
    register_blueprint(app, blueprint)


@app.errorhandler(404)
def not_found(error):
    return jsonify(message='Not found.'), 404


@app.after_request
def after_request(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp
