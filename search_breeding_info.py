import flask, flask.views
import os
import utils
from flask_sqlalchemy import SQLAlchemy
from models import *
from datetime import date

class search_breeding_info(flask.views.MethodView):

    __table__ = Breeding

    @utils.login_required
    def get(self):
        return flask.render_template('search_breeding_info.html')

    @utils.login_required
    def post(self):
        search_dict = {}
        search_list = []
        item = flask.request.form['bc']
        __table__ = Breeding
        search = __table__.query.filter_by(Breeding_Cage_Id = item).all()
        if len(search) == 0:
            flask.abort(404)
        else:
            for result in search:            
                search_dict = dict((col,getattr(result,col)) for col in result.__table__.columns.keys())
                search_list.append(search_dict)
#        search_dict = dict((col,getattr(search,col)) for col in search.__table__.columns.keys())
            return flask.render_template('search_breeding_info.html', search_list=search_list, search_dict=search_dict)
