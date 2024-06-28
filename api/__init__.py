import os
from flask import Flask
from .logger import log
from .routes import nltk_blueprint
from .nltk_downloader import downloader


# Move to config file if there are more global variables
NLTK_REQUIREMENTS = ['punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words']


def create_app() -> Flask:
    app = Flask(__name__)
    log(log.INFO, "App initialized: [%s]", app.__class__.__name__)

    # Prepare nltk.
    downloader(NLTK_REQUIREMENTS)

    # Register blueprints.
    app.register_blueprint(nltk_blueprint)

    return app
