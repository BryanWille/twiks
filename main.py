import services.database as db
import tweepy
import keys.keys as keys
import services.charts as ch
import json

def api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    
def retweet(api: tweepy.API, tweetID: int):
    api.retweet(tweetID);

def unretweet(api: tweepy.API, tweetID: int):
    api.unretweet(tweetID)
    
def getUserData(api: tweepy.API, username: str):
    return api.get_user(screen_name = username)

def getUserId(api: tweepy.API, username: str):
    return getUserData(api, username)._json['id_str'] 

def createUserDataBase(api: tweepy.API, user_name):
    db.Database.createUserInfo(getUserData(api, user_name)._json, user_name)

def createFavDataBase(api: tweepy.API, user_name):
    user = getUserData(api, user_name)._json
    favourite_count = api.get_favorites(id=user['screen_name'], count=user['favourites_count'])
    for favourites in favourite_count:
        db.Database.createStatusInfo(favourites._json, user_name)

def createStatusDataBase(api: tweepy.API, user_name):
    user_id = getUserId(api, user_name)
    for tweet in tweepy.Cursor(api.user_timeline,id=user_id).items():
        db.Database.createPostsInfo(tweet._json, user_name)
       
        
def createAllUserData(api: tweepy.API, user_name):
    user = api.get_user(screen_name = user_name)
    if not db.Database.doesUserExist(user_name, user._json['id_str']):
        createUserDataBase(api, user_name)
        createStatusDataBase(api, user_name)
        createFavDataBase(api, user_name)
    else:
        print("user already registered")
    
if __name__ == '__main__':
    api = api()
    user_name = "sr_wille"
    #createStatusDataBase(api, user_name)
    eu = ch.Charts(user_name)
    eu.mostCommonHour()
    
    #createAllUserData(api, user_name)

    
    