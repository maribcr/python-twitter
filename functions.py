import tweepy
from tweepy import OAuthHandler
import json
from apps.analytics_twitter.models import *
from django.utils import timezone

def connect(consumer_key, consumer_secret, access_token, access_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    return api


def search(projeto, consumer_key, consumer_secret, access_token, access_secret):
    try:
        api = connect(consumer_key, consumer_secret, access_token, access_secret)
    except Exception:
        raise

    for tag in projeto.get_hashtags():
        tag = "#" + tag.tag
        results = api.search(q=tag, count=2)
        list_tweets = []
        tweet = {}
        for key, result in enumerate(results):
            obj_tweet = result._json
            tweet[key + 1] = {}
            tweet[key + 1]["tweet"] = obj_tweet
            list_tweets.append(tweet[key + 1])
        print(json.dumps(list_tweets))

    # for pessoa in projeto.get_pessoas():
    #     print("@" + pessoa.username)


def get_user_info():
    try:
        consumer_key = 'vW4AcSrYBkRAeHzdVuu6pbqKc'
        consumer_secret = 'C2hhzPkJKk2bPZaW3s9xMy85AqOafdgxA7NDidIKy9JF6bGLw5'
        access_token = '2513377017-1ssVpFBXjMk06aBkDbXI3AbLgzZ88QMRCmrOhjT'
        access_secret = 'tENBULOt8eEg4EWqqwOZIiZaQtFOhTQWzq5KJWMPnR2O4'
        api = connect(consumer_key, consumer_secret, access_token, access_secret)

    except Exception:
        raise

    results = api.search_users(q='@oliveiraptk95')

    user = {}

    for result in results:
        obj_user = result._json
        user["user"] = obj_user

    print(json.dumps(user))


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        list_tweets = []
        tweet = {}
        tweet["tweet"] = status._json
        list_tweets.append(tweet["tweet"])

        print(json.dumps(list_tweets))


def stream(projeto, consumer_key, consumer_secret, access_token, access_secret):
    try:
        api = connect(consumer_key, consumer_secret, access_token, access_secret)
    except Exception:
        raise

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['patocada'], async=True)

    if timezone.now() >= projeto.final_date:
        myStream.disconnect()
