from flask import Blueprint

bp = Blueprint('courier', __name__, url_prefix='/courier')

from . import routes, models