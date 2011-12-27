from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.http import urlencode

def home(request):
	params = {}

	if request.GET.get('error'):
		params['error'] = request.GET.get('error')

	if request.GET.get('msg'):
		params['msg'] = request.GET.get('msg')

	if len(params) == 0:
		params = ''
	else:
		params = urlencode(params)

	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?' + params)

	if request.user.is_staff:
		return HttpResponseRedirect('/tweets/dashboard/?' + params)
	else:
		return HttpResponseRedirect('/tweets/?' + params)
