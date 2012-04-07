from django.template import RequestContext
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
import os

from userprofile.models import UserProfile
from userprofile.forms import UserProfileForm
from docmanager.forms import DocumentForm
from docmanager.models import Document

def serve(request, doc_id=None):
	doc = Document.objects.get(pk=doc_id)
	return HttpResponseRedirect('/%s' % doc.filename())

@login_required
def list(request):
	documents = Document.objects.all().order_by('-last_modified')

	return render_to_response('list.html', {
		'documents': documents,
	}, context_instance=RequestContext(request))

@login_required
def add(request):
	if request.POST:
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.creator = request.user
			f.last_edited_by = request.user
			f.save()
			return HttpResponseRedirect('/a/add/')
	else:
		lastdoc = Document.objects.all().order_by('-last_modified')[:1]
		form = DocumentForm(initial={'category':lastdoc[0].category})
	return render_to_response('add.html', {
		'form': form,
	}, context_instance=RequestContext(request))

@login_required
def edit(request, doc_id=None):
	doc = Document.objects.get(pk=doc_id)
	if request.POST:
		if request.FILES and doc.document:
				os.remove(doc.document.path)
				doc.document.delete()
		form = DocumentForm(instance=doc,data=request.POST,files=request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.last_edited_by = request.user
			f.save()
			return HttpResponseRedirect('/a/')
	else:
		form = DocumentForm(instance=doc)
	return render_to_response('add.html', {
		'form': form,
	}, context_instance=RequestContext(request))