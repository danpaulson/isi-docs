from django.forms import ModelForm
	
from docmanager.models import Document

class DocumentForm(ModelForm):
	class Meta:
		model = Document
		exclude = ('user','creator','last_edited_by','deleted','date_deleted')