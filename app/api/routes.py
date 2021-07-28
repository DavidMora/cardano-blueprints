from flask import jsonify, request, abort, make_response, current_app

from . import api
from ..controllers.command_executer import execute

# custom 404 error handler
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'detail': 'Not found'}), 404)


# custom 400 error handler
@api.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'detail': 'Bad request'}), 400)


@api.route('/executeMovements', methods=['POST'])
def executeMovements():
    commands = request.json.get('commands')
    return jsonify(execute(commands))
