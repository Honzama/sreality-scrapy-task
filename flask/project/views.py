from flask import jsonify, render_template

from project.extensions import db
from project.models import Flat


def render_flats():
    flats = []

    for flat in db.session.query(Flat).all():
        del flat.__dict__['_sa_instance_state']
        flats.append(flat.__dict__)

    return render_template("index.html", flats=flats)
