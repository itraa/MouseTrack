import flask, flask.views
import os
import sys
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask.ext.mail import Message
import datetime
from apscheduler.scheduler import Scheduler
import time

class add_breeding_info(flask.views.MethodView):
    
    db.create_all()
        
    @utils.login_required
    def get(self):
        return flask.render_template('add_breeding_info.html')
        
    @utils.login_required
    def post(self):
        input1 = Breeding(flask.request.form['bc'],
                           flask.request.form['maletag'],
                            flask.request.form['maledob'],
                            flask.request.form['female1tag'],
                            flask.request.form['female1dob'],
                            flask.request.form['female2tag'],
                            flask.request.form['female2dob'],
                            flask.request.form['dateofsetup'])

        db.session.add(input1)
        db.session.commit()
        flask.flash("The Breeding info has been successfully added")
        return flask.redirect(flask.url_for('add_pups_info'))        