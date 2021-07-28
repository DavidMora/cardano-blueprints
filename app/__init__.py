from flask import Flask
from flask_bootstrap import Bootstrap

from app.site.routes import site
from app.api.routes import api


bootstrap = Bootstrap()


def create_app(config_name):

    # create app instance
    app = Flask(__name__)

    # add configuration
    app.config.from_object(config_name)

    # register extensions
    bootstrap.init_app(app)

    # register blueprints
    app.register_blueprint(site)
    app.register_blueprint(api, url_prefix='/api')
    return app


