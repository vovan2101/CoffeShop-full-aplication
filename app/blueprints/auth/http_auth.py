from datetime import datetime
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from .models import User


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify(name, password):
    user = User.query.filter_by(name=name).first()######
    if user and user.check_password(password):
        return user

@token_auth.verify_token
def verify(token):
    user = User.query.filter_by(token=token).first()
    if user and user.token_expiration > datetime.utcnow():
        return user

