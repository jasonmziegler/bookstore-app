#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_type): #config_type = prod, test, dev (corresponds to file names)

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'app//config', config_type + '.py')

    app.config.from_pyfile(configuration)

    db.init_app(app) #bind database to flask app

    from app.catalog import main #import blueprint
    app.register_blueprint(main) #register blueprint

    return app
