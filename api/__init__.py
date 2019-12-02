from flask import Flask

from common import settings


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(settings)

    from api.index import index_blu
    app.register_blueprint(index_blu)
    return app
