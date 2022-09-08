from flask.cli import FlaskGroup

from project import app
from project.crawler import crawl_flats
from project.extensions import db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("load_flats")
def load_flats():
    crawl_flats()


if __name__ == "__main__":
    cli()
