from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import jsonify, request
import logging, app

logging.basicConfig(level=logging.INFO)


def token_required(fn):
    """Decorator to check if the request has a valid JWT token.

    Args:
        fn (function): Function to be decorated.
        
    Returns:
        function: Decorated function with token verification.
    """
    
    @wraps(fn)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception as e:
            logging.error(f"Token verification failed: {str(e)}")
            return jsonify({"message": "Token is missing or invalid!"}), 401
        
        return fn(*args, **kwargs)
    return decorated