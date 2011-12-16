from django.conf.urls.defaults import patterns, include, url
from retweeter import views
from retweeter import login
from retweeter import tweetmanager
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
		(r'^$', views.home),
		(r'^accounts/login/$', 'login.views.login', {'template_name': 'login.html'}),
		(r'^accounts/logout/$', logout, {'next_page': '/'}),
		(r'^accounts/register/$', 'login.views.register'),
		(r'^accounts/profile/$', 'login.views.profile'),

		(r'^tweets/$', 'tweetmanager.views.tweets'),
		(r'^tweets/submit/$', 'tweetmanager.views.tweets_submit'),

		(r'^tweets/dashboard/$', 'tweetmanager.views.dashboard'),

		(r'^tweets/moderate/$', 'tweetmanager.views.moderate'),
		(r'^tweets/moderate/approve/(\d+)/$', 'tweetmanager.views.approve'),
		(r'^tweets/moderate/disapprove/(\d+)/$', 'tweetmanager.views.disapprove'),
    # Examples:
    # url(r'^$', 'retweeter.views.home', name='home'),
    # url(r'^retweeter/', include('retweeter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
