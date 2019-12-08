from flask import Flask
from flask_cors import CORS

from common import settings


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(settings)
    CORS(app)

    from api.index import home_blu
    app.register_blueprint(home_blu)
    return app
