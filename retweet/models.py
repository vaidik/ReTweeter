from django.db import models

class Tweets(models.Model):
	status = models.CharField(max_length=140)
	twitter_id = models.CharField(max_length=25)
