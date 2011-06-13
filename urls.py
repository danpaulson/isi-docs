from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# (r'^django_template/', include('django_template.foo.urls')),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	#(r'^admin/(.*)', admin.site.root),
	url(r'^admin/', include(admin.site.urls)),

	(r'^robots\.txt$', direct_to_template,
		{ 	'template': 'robots.txt', 
			'mimetype': 'text/plain' }),
	(r'^humans\.txt$', direct_to_template,
		{ 	'template': 'humans.txt', 
			'mimetype': 'text/plain' }),
	(r'^template$', direct_to_template,
		{ 	'template': '_template.html', 
			'mimetype': 'text/html' }),
)
