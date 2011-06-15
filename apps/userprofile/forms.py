from django.forms import ModelForm

from userprofile.models import UserProfile

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('gender',)
