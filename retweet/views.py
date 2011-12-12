from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import twitter, helper
from forms import SubmitTweet
from models import Tweets
from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	else:
		if request.user.is_staff == True:
			return HttpResponseRedirect('/admin/home/')
		else:
			return HttpResponseRedirect('/user/tweet/')

@login_required
def admin_home(request):
	return HttpResponseRedirect('/admin/tweet/')

@login_required
def admin_tweet(request):
	rows = Tweets.objects.filter(twitter_id='')

	tweets = []
	for row in rows:
		tweet = {}
		tweet['id'] = row.id
		tweet['obj'] = row
		tweet['user'] = User.objects.get(id=row.user_id)

		tweets.append(tweet)

	val = {}
	val['user'] = request.user
	val['tweets'] = tweets
	val['form'] = SubmitTweet()

	return render_to_response('admin_home.html', val)

@login_required
def admin_tweet_approve(request, id):
	api = twitter.api_obj(settings.CONSUMER_KEY, settings.CONSUMER_SERET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

	tweet = Tweets.objects.get(id=id)
	msg = tweet.status

	try:
		tweet_id = twitter.tweet(api, msg)

		tweet.twitter_id = tweet_id
		tweet.save()
	except RuntimeError:
		pass

	return HttpResponseRedirect('/admin/home/')

@login_required
def admin_tweet_disapprove(request, id):
	tweet = Tweets.objects.get(id=id)
	tweet.delete()

	return HttpResponseRedirect('/admin/home/')

@login_required
def tweet(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	else:
		val = {}
		val['user'] = request.user
		val['form'] = SubmitTweet()

		return render_to_response('user_home.html', val)

@login_required
def tweet_submit(request):
	if request.method == 'POST':
		if request.POST.get('status', ''):
			helper.add_tweet(request.POST['status'], request.user)

	if request.user.is_staff == True:
		path = '/admin/tweet/'
	else:
		path = '/user/tweet/'

	return HttpResponseRedirect(path)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()

	return render_to_response("registration/register.html", {'form': form})
