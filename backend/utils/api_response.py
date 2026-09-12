from flask import jsonify


def success(message, status_code=200, data=None):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    }), status_code

def error(message, status_code=500, errors=None):
    return jsonify({
        "success": False,
        "message": message,
        "errors": errors
    }), status_code
