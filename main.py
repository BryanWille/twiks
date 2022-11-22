import json
import tweepy
import keys


def api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    api.get_favorites
    print("tweetei com sucesso!")
    

if __name__ == '__main__':
    api = api()
    likes_bernardo = api.get_favorites(id = 2882428500, count=30)
    for likes in likes_bernardo:
        try:
             api.unretweet(likes._json["id"])
             print("RT concluido")
        except:
            ""