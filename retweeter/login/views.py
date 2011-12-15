from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth.views import login as auth_login

def login(request, template_name):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	return auth_login(request, template_name)

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()

	return render_to_response("register.html", {'form': form}, context_instance=RequestContext(request))

def profile(request):
	return HttpResponseRedirect('/')
