from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import twitter
import helper

def home(request):
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/accounts/login/')
		else:
			val = {}
			val['user'] = request.user
			return render_to_response('user_home.html', val)

def tweet(request):
	return render_to_response('tweet.html', {})

def tweet_submit(request):
	helper.add_tweet(request.POST['status'])

	return HttpResponseRedirect('/')
