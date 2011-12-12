from django.conf import settings
from django.conf.urls.defaults import *
from retweeter.retweet import views
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.home),
    (r'^admin/home/$', views.admin_home),
    (r'^admin/tweet/$', views.admin_tweet),
    (r'^admin/tweet/submit/$', views.tweet_submit),
    (r'^admin/tweet/approve/(\d+)/$', views.admin_tweet_approve),
    (r'^admin/tweet/disapprove/(\d+)/$', views.admin_tweet_disapprove),
    (r'^user/tweet/$', views.tweet),
    (r'^user/tweet_submit/$', views.tweet_submit),
    (r'^accounts/login/$', login),
    (r'^accounts/register/$', views.register),
    (r'^accounts/logout/$', logout, {'next_page': '/'}),
)
