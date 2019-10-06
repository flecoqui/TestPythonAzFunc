""" Microservice main programm file """
##
#
# This file is the microservice itself.
#
##

# pylint: disable=invalid-name;
# In order to avoid false positives with Flask

from os import environ
from datetime import datetime
from flask import Flask, jsonify, make_response, url_for, request
import settings

# -- Application initialization. ---------------------------------------------

__modeConfig__ = environ.get('MODE_CONFIG') or 'Development'
APP = Flask(__name__)
APP.config.from_object(getattr(settings, __modeConfig__.title()))


# -- This function controls how to respond to common errors. -----------------

@APP.errorhandler(404)
def not_found(error):
    """ HTTP Error 404 Not Found """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 404, headers
    )


@APP.errorhandler(405)
def not_allowed(error):
    """ HTTP Error 405 Not Allowed """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 405, headers
    )


@APP.errorhandler(500)
def internal_error(error):
    """ HTTP Error 500 Internal Server Error """
    headers = {}
    return make_response(
        jsonify(
            {
                'error': 'true',
                'msg': str(error)
            }
        ), 500, headers
    )


# -- This piece of code controls what happens during the HTTP transaction. ---

@APP.before_request
def before_request():
    """ This function handles  HTTP request as it arrives to the API """
    pass


@APP.after_request
def after_request(response):
    """ This function handles HTTP response before send it back to client  """
    return response


# -- This is where the API effectively starts. -------------------------------

@APP.route('/', methods=['GET'])
def index():
    """
    This is the API index endpoint with HATEOAS support
    :param: none
    :return: a JSON (application/json)
    """

    headers = {}

    return make_response(
        jsonify(
            {
                'msg': 'this is index endpoint',
                'tstamp': datetime.utcnow().timestamp(),
                'endpoints': {
                    'url_echo': url_for('echo', _external=True)
                }
            }
        ), 200, headers
    )


@APP.route('/api/HttpTriggerPythonFunction', methods=['POST'])
@APP.route('/api/HttpTriggerPythonFunction/<string:item>', methods=['POST'])
def echo(**kwargs):
    """
    This is the ECHO endpoint with HATEOAS support
    :param kwargs: gets an item from the url as a string of any size and format
    :return: a JSON (application/json)
    """

    if kwargs:
        content = kwargs['item']
    else:
        content = 'none'

    if request.args.get('param1', type=str) is None:
        param1 = 'none'
    else:
        param1 = request.args.get('param1', type=str)
    if request.args.get('param2', type=str) is None:
        param2 = 'none'
    else:
        param2 = request.args.get('param2', type=str)

    
    req_body = request.get_json()

    if param2 == 'none':
        param2 = req_body.get('param2')
    if param1 == 'none':
        param1 = req_body.get('param1')
    
    headers = {}

    return make_response(
        jsonify(
            {
                'msg': 'this is an echo endpoint',
                'tstamp': datetime.utcnow().timestamp(),
                'namespace_params': {
                    'content_received': content,
                    'param1': param1,
                    'param2': param2
                    
                },
                'endpoints': {
                    'url_index': url_for('index', _external=True)
                }
            }
        ), 200, headers
    )


# -- Finally, the application is run, more or less ;) ------------------------

if __name__ == '__main__':
    APP.run()
