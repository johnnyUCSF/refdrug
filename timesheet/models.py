from django.db import models
from django.http import Http404
from django.shortcuts import render
###
import datetime
from datetime import date
from pytz import timezone
#############

class User(models.Model):
	""" Each user has a unique code and some identifying personal information.
		Each user owns multiple workdays.
	"""
	unique_code = models.IntegerField(unique=True)
	first_name 	= models.TextField(max_length=30)
	last_name 	= models.TextField(max_length=30)
	#### functions
	def __str__(self):
		return(self.first_name+' '+self.last_name)

class Workday(models.Model):
	""" Each Workday contains the time in and out for that day.
	"""
	user 		= models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	date 		= models.DateField(auto_now=True)
	time_in 	= models.TimeField(default=None)
	time_out 	= models.TimeField(default=None,null=True)
	total_time 	= models.FloatField(default=None,null=True)
	#### functions
	def __str__(self):
		full_name = self.user.first_name+' '+self.user.last_name+' | '
		return(full_name+str(self.date))

	def update_time_out(self,time_out):
		self.time_out = time_out
		self.save()

	def update_total_time(self):
		duration = datetime.datetime.combine(date.min, self.time_out) - datetime.datetime.combine(date.min, self.time_in)
		duration_in_s = duration.total_seconds()
		hours = divmod(duration_in_s, 3600)[0] 
		### save
		self.total_time = hours
		print(hours,duration_in_s)

###### functions

def ENTRY(entry_code):
	""" Takes in entry of timestamp code and adds to database."""
	if check_user(entry_code) ==True:
		###workday = Workday.objects.filter(date=get_time()).get()
		enter_workday(entry_code)

def check_user(entry_code):
	""" Check if user timestamp code is an existing code."""
	if len(User.objects.filter(unique_code=entry_code)) == 1:
		return(True)
	else:
		raise Http404('No users exist with this code.')

def check_time_out(usernow,datenow):
	""" Chek if time out has been entered already. """
	if usernow.workday_set.filter(date=datenow).get().time_out == None:
		return(True)
	else:
		raise Http404('Leaving time has already been entered for this day!')

def get_time():
	""" Gets current time formats and returns."""
	eastern = timezone('US/Eastern')
	now = datetime.datetime.now(eastern).time()
	return(now) 

def enter_workday(entry_code):
	### get user and date first
	usernow = User.objects.filter(unique_code=entry_code).get()
	datenow = date.today()
	###
	if len(usernow.workday_set.filter(date=datenow))==1:
		if check_time_out(usernow,datenow) == True:
			### entry exists, means you are adding a date out
			usernow.workday_set.filter(date=datenow).get().update_time_out(get_time())
			usernow.workday_set.filter(date=datenow).get().update_total_time()
	else:
		### entry does not exist, means you have to add a new day
		usernow.workday_set.create(time_in=get_time())




