import flask,flask.views
import settings
import os
import utils
from apscheduler.scheduler import Scheduler
import datetime
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mail import Message
from main import Main
from login import Login
from models import *
from add_breeding_info import *
from add_pups_info import *
from search_breeding_info import *
from search_pups_info import *
from remove_breeding_info import *
#from calculate_weaning import *

app.secret_key =  settings.secret_key
main_view_func = Main.as_view('main')

# Routes
app.add_url_rule('/',
                 view_func=main_view_func,
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=main_view_func,
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])

app.add_url_rule('/add_breeding_info/',
                view_func=add_breeding_info.as_view('add_breeding_info'), 
                methods=['GET','POST'])

app.add_url_rule('/add_pups_info/',
                view_func=add_pups_info.as_view('add_pups_info'), 
                methods=['GET','POST'])

app.add_url_rule('/search_breeding_info/',
                view_func=search_breeding_info.as_view('search_breeding_info'), 
                methods=['GET','POST'])

app.add_url_rule('/search_pups_info/',
                view_func=search_pups_info.as_view('search_pups_info'), 
                methods=['GET','POST'])

app.add_url_rule('/remove_breeding_info/',
                view_func=remove_breeding_info.as_view('remove_breeding_info'), 
                methods=['GET','POST'])

#app.add_url_rule('/calculate_weaning/',
#                view_func=calculate_weaning.as_view('calculate_weaning'), 
#                methods=['GET'])

def weaning_reminder():

    global Login.username
    print "Test %s" % Login.username
    __table__ = pups_info
    first_output = __table__.query.with_entities(__table__.Pups_Breeding_Cage_Id).filter_by(First_Date_of_weaning=date.today()).all()
    final_output = __table__.query.with_entities(__table__.Pups_Breeding_Cage_Id).filter_by(Final_Date_of_weaning=date.today()).all()
    
    first_email_list = []
    final_email_list = []

    if final_output:
        for final_each in final_output:
            for i in range(len(final_each)):
                final_email_list.append(str(final_each[i]))

        final_msg = Message('Final weaning reminder!',
                    sender='itraa.narayan@gmail.com.com',
                    recipients=['itraa.narayan@gmail.com'])
        final_msg.body = 'This is the final reminder for weaning pups from the breeding cage(s): %s' % final_email_list

        mail.send(final_msg)

    if first_output:
        for first_each in first_output:
            for i in range(len(first_each)):
                first_email_list.append(str(first_each[i]))

        first_msg = Message('First weaning reminder!',
                    sender='itraa.narayan@gmail.com.com',
                    recipients=['itraa.narayan@gmail.com'])
        first_msg.body = 'This is the first reminder for weaning pups from the breeding cage(s): %s' % first_email_list

        mail.send(first_msg)


weaning_reminder() 
#sched = Scheduler()
#sched.start()
#job = sched.add_cron_job(weaning_reminder, hour=23)

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
use_reloader=False
app.run()