from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError

def validate_schema(json_schema=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if json_schema:
                    validate_data = json_schema(**request.json)
                else:
                    return jsonify({"error": "no schema provided"}), 400
            except ValidationError as e:
                return jsonify({"error": e.errors()}), 400
            
            return func(*args, **kwargs, validate_data=validate_data)
        return wrapper
    return decorator
