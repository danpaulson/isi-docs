from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from common.models import BaseModel

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
)

class UserProfile(BaseModel):
	user = models.ForeignKey(User)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	
	def __unicode__(self):
		return '%s' % self.user
		
def create_userprofile(sender, instance, created, **kwargs):
	try:
		UserProfile.objects.get(user=instance)
	except:
		try:
			UserProfile.objects.create(user=instance)
		except:
			pass
post_save.connect(create_userprofile, sender=User)