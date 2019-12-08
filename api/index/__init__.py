from flask import Blueprint

home_blu = Blueprint('index', __name__)

from . import views
