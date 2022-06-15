from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine

db = SQLAlchemy()


def init_app(app: Flask):
    db_uri = app.config["SQLALCHEMY_DATABASE_URI"]
    engine = create_engine(db_uri)
    if not database_exists(engine.url):
        create_database(engine.url)

    db.init_app(app)
    app.db = db
