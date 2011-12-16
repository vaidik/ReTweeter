from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from retweeter.tweetmanager.forms import TweetForm
from retweeter.tweetmanager.models import Tweets
from retweeter.utils.helpers import render_page
from retweeter.tweetmanager import twitter
from django.utils.http import urlencode
import datetime

@login_required
def tweets(request):
	user = User.objects.get(username=request.user.username)

	t = Tweets.objects.order_by('-datetime').filter(user=user)
	form = TweetForm()

	return render_page('tweets.html', {'tweets': t, 'form': form}, request)

@login_required
def tweets_submit(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=/tweets/')

	user = User.objects.get(username=request.user.username)
	t = Tweets(tweet=request.POST.get('tweet'), status=0, user=user)

	params = ''
	try:
		t.save()
		params = urlencode({'msg': 'Your tweet was successfully submitted for review.'})
	except:
		params = urlencode({'error': 'Your tweet could not be submitted for review. Please make sure that the length of your tweet is less than 140 characters.'})

	return HttpResponseRedirect('/tweets/?' + params)

@login_required
def moderate(request):
	if not request.user.is_staff:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	data = {}

	t = Tweets.objects.filter(status=0)
	data['tweets'] = t

	return render_page('moderate.html', data, request)

@login_required
def dashboard(request):
	if not request.user.is_staff:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	data = {}

	t = Tweets.objects.filter(status=0)
	data['pending'] = len(t)

	return render_page('dashboard.html', data, request)

@login_required
def approve(request, tweet_id):
	if not request.user.is_staff:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	t = Tweets.objects.get(id=tweet_id)

	try:
		api = twitter.api_obj(settings.CONSUMER_KEY, settings.CONSUMER_SERET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
		tweet_id = twitter.tweet(api, t.tweet)

		t.twitter_id = tweet_id
		t.status = 1
		t.approver = User.objects.get(username=request.user.username)
		params = urlencode({'msg': 'The tweet was successfully published on Twitter.com.'})
	except:
		params = urlencode({'error': 'The tweet could not be published on Twitter.com. Please try again after some time.'})

	t.save()

	return HttpResponseRedirect('/tweets/moderate/?' + params)

@login_required
def disapprove(request, tweet_id):
	if not request.user.is_staff:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	t = Tweets.objects.get(id=tweet_id)
	t.status = -1
	t.approver = User.objects.get(username=request.user.username)
	t.save()

	params = urlencode({'msg': 'The tweet was successfully rejected.'})
	return HttpResponseRedirect('/tweets/moderate/?' + params)
