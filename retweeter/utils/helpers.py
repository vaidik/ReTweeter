from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def render_page(template_name, data, request):
	data['error'] = request.GET.get('error')
	data['msg'] = request.GET.get('msg')
	data['globals'] = {}
	data['globals']['twitter_account'] = settings.TWITTER_ACCOUNT

	return render_to_response(template_name, data, context_instance=RequestContext(request))
