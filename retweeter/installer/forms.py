from django import forms
from django.conf import settings
import os

class InstallationDetailsForm(forms.Form):
	twitter_account = forms.CharField(label='Twitter Account')
	twitter_consumer_key = forms.CharField(label='Consumer Key')
	twitter_consumer_secret = forms.CharField(label='Consumer Secret')

	def save(self):
		contents = ""

		contents += "TWITTER_ACCOUNT = '" + self.cleaned_data['twitter_account'] + "'\n"
		contents += "TWITTER_CONSUMER_KEY = '" + self.cleaned_data['twitter_consumer_key'] + "'\n"
		contents += "TWITTER_CONSUMER_SECRET = '" + self.cleaned_data['twitter_consumer_secret'] + "'\n"

		file = open(os.path.join(settings.APP_ROOT, 'app_settings.py'), 'w')
		file.write(contents)
		file.close()

