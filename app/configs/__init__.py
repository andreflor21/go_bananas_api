from flask import Flask
from flask_cors import CORS


def init_app(app: Flask):

    from . import env, database, migrations, jwt

    env.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    CORS(app)
