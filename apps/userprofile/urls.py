from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/update/profile/?$', 'userprofile.views.update_user_profile', name='update_user_profile'),
	url(r'^', 'userprofile.views.index', name='userprofile_index'),
)
