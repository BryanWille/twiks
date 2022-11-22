import tweepy
import keys

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(keys.access_token, keys.access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# using get_user with id
_id = "bernardobkt"
user = api.get_user(_id)
  
# printing the name of the user
print("The id " + _id +
      " corresponds to the user with the name : " +
      user.name)