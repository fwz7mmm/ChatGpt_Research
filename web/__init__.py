# project/__init__.py
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from web.models import data_models
    from . import models, routes, services
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    #models.init_app(app)
    routes.init_app(app)
    #services.init_app(app)
    with app.app_context():
        db.create_all()
        return app
    data1 = Data.query.all()