import tweepy
import keys
from tweepy import user;

def api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    print("tweetei com sucesso!")
    

if __name__ == '__main__':
    api = api()
    #tweet(api, "Isso foi twiteado do python")
    resposta = tweepy.Client.get_liked_tweets(
    "Tweepy", id=["bernardokbt"])
    print(resposta)