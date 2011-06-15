from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^userprofile/', include('userprofile.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/?$', 'django.contrib.auth.views.login', name="login"),
	url(r'^accounts/logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

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
