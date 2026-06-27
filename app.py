from flask import Flask

from config import Config
from database.database import db
from routes.api import api_bp
from routes.history import history_bp
from routes.home import home_bp
from routes.speech import speech_bp
from routes.translate import translate_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["DOWNLOAD_FOLDER"].mkdir(exist_ok=True)

    db.init_app(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()

    return app


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(translate_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(speech_bp)
    app.register_blueprint(api_bp, url_prefix="/api")


app = create_app()
