from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from retweeter.tweetmanager.models import Tweets
from django.contrib.auth.models import User
from django.template import RequestContext
from retweeter.tweetmanager.forms import TweetForm
import datetime

@login_required
def tweets(request):
	user = User.objects.get(username=request.user.username)
	t = Tweets.objects.order_by('-datetime').filter(user=user, status=0)

	form = TweetForm()

	return render_to_response('tweets.html', {'tweets': t, 'form': form}, context_instance=RequestContext(request))

def tweets_submit(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/?next=/tweets/')

	user = User.objects.get(username=request.user.username)
	t = Tweets(tweet=request.POST.get('tweet'), status=0, user=user)

	t.save()
	return HttpResponseRedirect('/tweets/?msg=success')
	#return HttpResponseRedirect('/tweets/?error')
