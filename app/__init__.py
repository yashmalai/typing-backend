from flask import Flask
from app.config import Config
from app.extension import db, migrate
from app.blueprints_registration import register_blueprints
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)
    return app