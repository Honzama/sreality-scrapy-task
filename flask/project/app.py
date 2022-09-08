from flask import Flask

from .views import render_flats
from .extensions import db


def register_extensions(app):
    db.init_app(app)


def add_views(app):
    app.add_url_rule('/', view_func=render_flats)


def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")

    register_extensions(app)
    add_views(app)

    return app


app = create_app()
