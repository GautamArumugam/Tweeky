import tweepy
import time

#First you have to create a twitter developer account and then have to create an app, in the app section you'll find keys and tokens.
#In the keys and tokens section:-
#Copy the first API key and API secret key and paste it below 
auth = tweepy.OAuthHandler('', '')
#Then copy the Access token and Access token secret and paste it below
auth.set_access_token('', '')

api = tweepy.API(auth)
user = api.me()

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(300)

#Be nice to your followers. Follow everyone!
#You can follow the people who followed you
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()

search = "Keyword Here" #Type the keyword here
numberOfTweets = 2 #No of posts you want to fetch with the above keyword
# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break