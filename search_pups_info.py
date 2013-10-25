import flask, flask.views
import os
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *
from datetime import date

class search_pups_info(flask.views.MethodView):

    __table__ = Breeding

    @utils.login_required
    def get(self):
        return flask.render_template('search_pups_info.html')

    @utils.login_required
    def post(self):
        search_dict = {}
        __table__ = pups_info
        item = flask.request.form['bc']
        search = __table__.query.filter_by(Pups_Breeding_Cage_Id = item).all()
        search_list = []
        if len(search) == 0:
            flask.abort(404)
        else:
            for result in search:            
                search_dict = dict((col,getattr(result,col)) for col in result.__table__.columns.keys())
                search_list.append(search_dict)
        return flask.render_template('search_pups_info.html', search_list=search_list, search_dict=search_dict)
