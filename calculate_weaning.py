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

class calculate_weaning(flask.views.MethodView):
    

#    def index(self,mail_breeding_cage,first_weaning_date):
#    def index(self):
 
#        msg = Message('Weaning Reminder!',
#                  sender='itraa.narayan@gmail.com.com',
#                  recipients=['itraa.narayan@gmail.com'])
#        msg.body = 'This is a reminder for weaning pups from the breeding cage id:'
#        if weaning date is today send the mail
#        if date.today() in Breeding.query.order_by(Breeding_cage_id, First_date_of_weaning):
#            mail.send(msg)
    

    def get(self):
        output = Breeding.query.filter(First_Date_of_weaning=date.today()).order_by(Breeding.Breeding_Cage_Id
#        output_dict = dict((col,getattr(output,col)) for col in output.__table__.columns.keys())
#        output = Breeding.query.order_by(Breeding.Breeding_Cage_Id, Breeding.First_Date_of_weaning)    
#        if date.today() in output:
#        return flask.render_template('calculate_weaning.html',output=output)
#       else:
#            flask.flash("None")
#            return flask.render_template('calculate_weaning.html')    
#        sched = Scheduler()
#       sched.start()
#        exec_date = date(2013, 9, 27)
#        job = sched.add_date_job(self.index, exec_date)
#        while True:
#            time.sleep(1)
#            sys.stdout.write('.'); sys.stdout.flush()

#        print exec_date
# The job will be executed on first weaning date and final weaning date
#        first_exec_date = datetime.date(*map(int,first_weaning_date.split('-')))
#        final_exec_date = datetime.date(*map(int,final_weaning_date.split('-')))

# Store the job in a variable in case we want to cancel it
        
#        job = sched.add_date_job(lambda:index(mail_breeding_cage,final_weaning_date), final_exec_date)
#        job = sched.add_cron_job(lambda:index(), month='9', day='25', hour='18')


#    def post(self):
#        output = Breeding.query.order_by(Breeding.Breeding_Cage_Id, Breeding.First_Date_of_weaning)         
#        return flask.render_template('calculate_weaning.html', output=output)
#    sched = Scheduler()
#        sched.start()
#        exec_date = date(2013, 9, 27)
#        job = sched.add_date_job(self.index, date.today())
#        flask.flash("Weaning reminder setup")
#        output = Breeding.query.order_by(Breeding_cage_id, First_date_of_weaning)            
#        return flask.render_template('search_breeding_info.html', output=output)
