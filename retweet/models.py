from django.db import models
from django.contrib.auth.models import User

class Tweets(models.Model):
	status = models.CharField(max_length=140)
	twitter_id = models.CharField(max_length=25)
	user = models.ForeignKey(User)
