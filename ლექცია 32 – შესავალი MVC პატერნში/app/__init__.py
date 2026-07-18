from flask import Flask

from app.config import Config
from app.controllers.main_controller import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_bp)
    return app
