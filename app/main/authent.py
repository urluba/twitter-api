from flask import abort, request
from functools import wraps
# from app import db
from app.models.user import User
import logging

def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')

        if not api_key:
            abort(401)

        user = User.query.filter_by(api_token=api_key).first()

        if not user:
            logging.debug('Unknown user')
            abort(401)

        logging.debug(
            'Current user %s (id %s)',
            user.username,
            user.id
        )

        return view_function(*args, **kwargs, user=user)

    return decorated_function
