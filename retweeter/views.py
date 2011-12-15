from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')

	return render_to_response('base.html')
