from django.template import RequestContext
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from userprofile.models import UserProfile
from userprofile.forms import UserProfileForm

def index(request):
	users = User.objects.all()
	
	return render_to_response('userprofile/index.html', {
		'users': users,
	}, context_instance=RequestContext(request))

@login_required
def update_user_profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)

	if request.user == user or request.user.is_superuser:
		up = UserProfile.objects.get_or_create(user=user, defaults={ 'user' : user })
		userprofile = up[0]
		
		if request.method == 'POST':
			f = UserProfileForm(request.POST, instance=userprofile)
			if f.is_valid():
				try:
					f.save()
				except:
					messages.error(request,'There was a problem updating the user profile.')
				else:
					messages.success(request,'User profile updated successfully!.')
		f = UserProfileForm(instance=userprofile)
	
		return render_to_response('userprofile/update_user_profile.html', {
			'form': f,
		}, context_instance =  RequestContext(request))
	else:
		return HttpResponseForbidden('You do not have access to this page.')