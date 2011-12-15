from django.db import models
from django.contrib.auth.models import User

class Tweets(models.Model):
	STATUS_CHOICES = (
		(-1, -1),
		(0, 0),
		(1, 1),
	)

	tweet = models.CharField(max_length=140)
	status = models.IntegerField(choices=STATUS_CHOICES)
	datetime = models.DateTimeField(auto_now_add=True)
	twitter_id = models.CharField(max_length=25)
	user = models.ForeignKey(User, related_name='tweets')
	approver = models.ForeignKey(User, null=True, related_name='tweets_approved')
