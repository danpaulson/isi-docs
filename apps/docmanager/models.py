from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
import os.path
from common.models import BaseModel

class Document(BaseModel):
	creator = models.ForeignKey(User,related_name='creator')
	category = models.ForeignKey('Category',related_name='category')
	last_edited_by = models.ForeignKey(User,related_name='lastedit_user')
	title = models.CharField(max_length = 100)
	document = models.FileField(upload_to=settings.UPLOAD_DIR)

	def __unicode__(self):
		return '%s' % self.title

	def filename(self):
		return os.path.basename(self.document.name)

class Category(BaseModel):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return '%s' % self.name