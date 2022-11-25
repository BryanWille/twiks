import services.database as db
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

def getAllLikes(api: tweepy.API, user_id, like_count: int):
    return api.get_favorites(id=user_id, count=like_count)

def createUserDataBase(api: tweepy.API, user_name):
    db.Database.createUserInfo(getUserData(api, user_name)._json)

def createFavDataBase(api: tweepy.API, user_name):
    user = getUserData(api, user_name)._json
    favourite_count = getAllLikes(api, user['screen_name'], user['favourites_count'])
    for c in range(0, len(favourite_count)):
        db.Database.createStatusInfo(favourite_count[c]._json, user_name)
    
if __name__ == '__main__':
    api = api()
    user_name = "sr_wille"
    createUserDataBase(api, user_name=user_name)
    createFavDataBase(api, user_name)

    #fav_list = db.Database.retrieveStatusInfo(username=user_name)
    #print(fav_list)
    