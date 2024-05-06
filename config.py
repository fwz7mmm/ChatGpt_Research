import os
basedir = os.path.abspath(os.path.dirname(__file__))
import sqlite3
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
