from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	(r'^userprofile/', include('userprofile.urls')),
	(r'^files/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT } ),

	url(r'^a/', include('docmanager.urls')),
	url(r'^d/(?P<doc_id>\d+)?$', 'docmanager.views.serve', name='doc_serve'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/?$', 'django.contrib.auth.views.login', name="login"),
	url(r'^accounts/logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

	url(r'^(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT+'/uploads/'  } ),

	(r'^robots\.txt$', direct_to_template,
		{ 	'template': 'robots.txt', 
			'mimetype': 'text/plain' }),
	(r'^humans\.txt$', direct_to_template,
		{ 	'template': 'humans.txt', 
			'mimetype': 'text/plain' }),
	(r'^template$', direct_to_template,
		{ 	'template': '_template.html', 
			'mimetype': 'text/html' }),
	(r'^$', direct_to_template,
		{ 	'template': 'index.html', 
			'mimetype': 'text/html' }),
)
