from flask import Flask
from config import config

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize any extensions or blueprints here
    # For example: db.init_app(app)

    # Import and register blueprints here
    # For example: from .routes import main_blueprint
    #              app.register_blueprint(main_blueprint)

    # Import modules for ASR, NLP, authentication, transaction handling, and utilities
    from . import asr, nlp, authentication, transaction_handler, utils

    return app
