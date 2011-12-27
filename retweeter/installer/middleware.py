from django.http import HttpResponse, HttpResponseRedirect
from retweeter.installer.helpers import check_app_settings, check_db_settings

class CheckInstallation(object):
	allowed_urls = [
		'/install/',
		'/authorize/',
	]

	def process_request(self, request):
		if not check_db_settings() or not check_app_settings():
			if request.META['PATH_INFO'] not in self.allowed_urls:
				return HttpResponseRedirect('/install/')
