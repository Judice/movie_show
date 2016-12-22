# _*_ coding: utf-8 _*_
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    from .views import main_blueprint, auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
