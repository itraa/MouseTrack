import flask, flask.views
import os
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *

class remove_breeding_info(flask.views.MethodView):

    @utils.login_required
    def get(self):
        return flask.render_template('remove_breeding_info.html')

    @utils.login_required
    def post(self):
        item = flask.request.form['bc']
        search = Breeding.query.filter_by(Breeding_Cage_Id = item).first_or_404()
        db.session.delete(search)
        db.session.commit()
        flask.flash("The Breeding info for the Cage %s has been deleted" % item)
        return flask.render_template('remove_breeding_info.html')
