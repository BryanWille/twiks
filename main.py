import services.database as db
import models.user as twitteruser
import json
import tweepy
import keys.keys as keys



def api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    api.get_favorites
    print("tweetei com sucesso!")
    
def retweet(api: tweepy.API, tweetID: int):
    api.retweet(tweetID);

def unretweet(api: tweepy.API, tweetID: int):
    api.unretweet(tweetID)
    
def getUserData(api: tweepy.API, username: str):
    return api.get_user(screen_name = username)

def writeDataJson(data, filename = str):
    file = open(filename+".json", "w")
    file.write(json.dumps(data))


if __name__ == '__main__':
    api = api()
    usuario = getUserData(api, "bernardokbt")
    pessoa = twitteruser.User.mapToUser(user_map=usuario._json)
    mapa_pessoa = pessoa.userToMap()
    db.Database.createUserInfo(mapa_pessoa)