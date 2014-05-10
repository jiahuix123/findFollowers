'''
Created on May 9, 2014

@author: Jiahui Xu
'''
import tweepy
# The app is not working
auth = tweepy.OAuthHandler("pLE7Y091zOA5XCqduUAAbWBeW", "C6UZ9T7SsU3H9nxQR2SZHImrJxgmseSFHY1V12QGVR9gOqrxjC")
auth.set_access_token("2486783642-Ff6zxAkAOFXYUIhPJBW9WkyUeZtglVhcsAtj5cH", "PC67AEUcdtyzrhmyoY8nDRtBdP7RnXXKvTOUHmhNYQ3qd")
api = tweepy.API(auth)

# prints out the total number of followers the specific user has, 
# and also prints out each follower's total number of followers in 1 deep level
def get_twitter_users(user_id):
    totalFollower = api.get_user(user_id).followers_count()
    print totalFollower    
    # print out the number of followers for each follower
    listOfFriends = api.followers(user_id)
    for x in listOfFriends:
        followersCount = api.get_user(x).followers_count()
        print followersCount