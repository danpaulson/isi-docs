from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
from django.contrib.auth.models import User

import userprofile.models as upm

def create_initial_userprofile(sender, **kwargs):
	'''
	This is a one-time script only used to create the initial superuser profile.
	
	Why?
	The initial ./manage.py syncdb creates all the base tables and creates the first superuser account.
	There is a post_save signal in userprofile.models to automatically create a userprofile whenever a user is created.
	
	The Problem?
	The userprofile app is managed using migrations with South so the tables don't get created until you run ./manage migrate the first time (after you've run syncdb the first time).
	This script will get run everytime you run ./manage.py migrate, but it will only create the UserProfile if one doesn't exist.
	'''
	
	u = User.objects.get(pk=1)
	try:
		upm.UserProfile.objects.get(user=u)
	except:
		print "Creating initial superuser profile."
		upm.UserProfile.objects.create(user=u)
post_syncdb.connect(create_initial_userprofile, sender=upm)