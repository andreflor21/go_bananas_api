from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import configs

    configs.init_app(app)

    from app import views

    views.init_app(app)

    return app
