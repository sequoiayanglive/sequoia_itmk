from flask import Blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

from .demo import api_demo_hello
from .demo import api_bicolor_sphere