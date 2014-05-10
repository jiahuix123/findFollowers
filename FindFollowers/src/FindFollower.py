'''
Created on May 9, 2014

@author: Jiahui Xu
'''
import tweepy

auth = tweepy.OAuthHandler("pLE7Y091zOA5XCqduUAAbWBeW", "C6UZ9T7SsU3H9nxQR2SZHImrJxgmseSFHY1V12QGVR9gOqrxjC")
auth.set_access_token("2486783642-Ff6zxAkAOFXYUIhPJBW9WkyUeZtglVhcsAtj5cH", "PC67AEUcdtyzrhmyoY8nDRtBdP7RnXXKvTOUHmhNYQ3qd")
api = tweepy.API(auth)

# prints out the total number of followers the specific user has, 
# and also prints out each follower's total number of followers in 1 deep level
def get_twitter_users(user_id):
    print api.get_user(user_id).followers_count
    # print out the number of followers for each follower
    for eachUser in tweepy.Cursor(api.followers, screen_name = user_id).items():
        print eachUser.screen_name, eachUser.followers_count

print "first example: an empty account"
get_twitter_users('tuziCarol') # my empty account, used for testing
print "second example: lokeshd's account"
get_twitter_users('lokeshd')
