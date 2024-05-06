import sys

from web import create_app

from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy


app = create_app()
app.debug = True

if __name__ == '__main__':
    app.run()