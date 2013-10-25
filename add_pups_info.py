import flask, flask.views
import os
import sys
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *
import datetime
import time

class add_pups_info(flask.views.MethodView):
    
    @utils.login_required
    def get(self):
        return flask.render_template('add_pups_info.html')
        
    @utils.login_required
    def post(self):
        pups_born_date = flask.request.form['datepupsborn']
        input2 = pups_info(flask.request.form['bc'],
                            flask.request.form['datepupsborn'],
                            datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=21),
                            datetime.date(*map(int, pups_born_date.split('-'))) + datetime.timedelta(days=28))
        db.session.add(input2)
        db.session.commit()
        flask.flash("The pups info has been successfully added")
        return flask.redirect(flask.url_for('add_pups_info'))