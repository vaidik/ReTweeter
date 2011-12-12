from django.conf import settings
from django.conf.urls.defaults import *
from retweeter.retweet import views
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.home),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {'next_page': '/'}),
)
