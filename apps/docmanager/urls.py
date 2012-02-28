from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^add/?$', 'docmanager.views.add', name='doc_add'),
	url(r'^edit/(?P<doc_id>\d+)?$', 'docmanager.views.edit', name='doc_edit'),
	url(r'^', 'docmanager.views.list', name='doc_list'),
)
