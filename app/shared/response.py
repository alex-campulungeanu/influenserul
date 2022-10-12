import json
from http import HTTPStatus

from flask import Response, jsonify

def response_success(msg, code=HTTPStatus.OK):
    return jsonify({'status': True, 'msg': msg, 'status_code': code}), code

def response_fail(msg, code=HTTPStatus.BAD_REQUEST):
    return jsonify({'status': False, 'msg': msg, 'status_code': code}), code

def response_data(data, code=HTTPStatus.OK):
    #  "default=str" is needed here to serialize a timedate column, see https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844
    return Response(json.dumps(data, default=str), mimetype="application/json", status=200)