import tweepy
import keys.keys as keys

class Api:
    def api():
        auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)

        return tweepy.API(auth)