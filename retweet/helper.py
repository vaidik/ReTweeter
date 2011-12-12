import twitter
from models import Tweets

def add_tweet(status, user):
	tweet = Tweets(status=status, user=user)
	tweet.save()
