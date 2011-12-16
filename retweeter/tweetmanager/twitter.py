import tweepy

def api_obj(consumer_key, consumer_secret, access_token, access_token_secret):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def tweet(api, msg):
	tweet = api.update_status(msg)

	return tweet.id

def retweet(api, status_id):
	retweet = api.retweet(status_id)

	return retweet.id
