from flask import Flask
from talkshow import blueprints, ext


def create_app(**kwargs):
    """Creates a new Flask app using the Factory Pattern"""
    app = Flask(__name__)
    app.config.update(kwargs)
    # extensions
    ext.configure(app)  #
    # blueprints
    blueprints.configure(app) 
    return app
