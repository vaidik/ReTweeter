import tweepy

def api_obj(consumer_key, consumer_secret, access_token, access_token_secret):
	#consumer_key="Ifr49NXWornWNpk7tW4JEg"
	#consumer_secret="qWd3u6K9zF1cRGogqO29AKTsJkQ9pluG133YczUprg"

	#access_token="97657711-4JY2SigScYzjSGDRLBvpMLUJuSs3tph8ZLbsQpEbq"
	#access_token_secret="bezvNQ7CNNyNKF7CpWtr1ucEKuzRJzC2Vl2sUjy0urw"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def tweet(api, msg):
	tweet = api.update_status(msg)

	return tweet.id

def retweet(api, status_id):
	retweet = api.retweet(status_id)

	return retweet.id
