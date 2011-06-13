from django.db import models

class SoftDeleteManager(models.Manager):
	''' Use this manager to get objects that have a deleted field '''
	def get_query_set(self):
		return super(SoftDeleteManager, self).get_query_set().filter(deleted=False)
	def all_with_deleted(self):
		return super(SoftDeleteManager, self).get_query_set()
	def deleted_set(self):
		return super(SoftDeleteManager, self).get_query_set().filter(deleted=True)

class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, db_index=True, null=True, blank=True)
	last_modified = models.DateTimeField(auto_now=True, db_index=True, null=True, blank=True)
	deleted = models.BooleanField(default = False, db_index=True)
	date_deleted = models.DateTimeField(null = True, blank = True, db_index=True)
	objects = SoftDeleteManager()

	class Meta:
		abstract = True
		
	def delete(self):
		from datetime import datetime
		
		self.deleted = True
		self.date_deleted = self.last_modified
		self.save()