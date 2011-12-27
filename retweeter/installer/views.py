from django.http import HttpResponse, HttpResponseRedirect
from retweeter.installer.forms import InstallationDetailsForm
from retweeter.utils.helpers import render_page
from subprocess import Popen
import shlex, os
from django.conf import settings
from django.core.management import call_command
import tweepy
from retweeter.installer.helpers import check_db_settings, check_app_settings
from retweeter import app_settings as settings

def install(request):
	if request.method == 'POST':
		form = InstallationDetailsForm(request.POST)
		if form.is_valid():
			auth = tweepy.OAuthHandler('Ifr49NXWornWNpk7tW4JEg', 'qWd3u6K9zF1cRGogqO29AKTsJkQ9pluG133YczUprg', 'http://www.google.com')
			url = auth.get_authorization_url()
			request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)

			return HttpResponseRedirect(url)

		return render_page('test.html', {'form': form}, request)
	else:
		if not check_db_settings():
			return render_page('database_missing.html', {}, request)

		if not check_app_settings():
			form = InstallationDetailsForm()
			return render_page('app_settings_missing.html', {'form': form}, request)

def authorize(request):
	if request.GET.get('oauth_token', '') and request.GET.get('oauth_verifier', ''):
		verifier = request.GET.get('oauth_verifier')
		auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
		token = request.session['request_token']
		del request.session['request_token']

		auth.set_request_token(token[0], token[1])

		try:
			auth.get_access_token(verifier)
		except tweepy.TweepError:
			print 'Error! Failed to get access token.'

		f = open(os.path.join(settings.APP_ROOT, 'app_settings.py'), 'a')
		f.write("TWITTER_ACCESS_TOKEN='%s'\n" % auth.access_token.key)
		f.write("TWITTER_ACCESS_SECRET='%s'\n" % auth.access_token.secret)
		f.close()

		return HttpResponseRedirect('/')

