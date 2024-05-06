from web.routes.home import home_blue
from web.routes.statistic import statistics_blue
from flask import Flask

app = Flask(__name__)

def init_app(app):
    app.register_blueprint(home_blue)
    app.register_blueprint(statistics_blue)