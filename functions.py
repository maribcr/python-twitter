import tweepy, json
from tweepy import OAuthHandler, auth


def connect(projeto):
    consumer_key = projeto.app.consumer_key
    consumer_secret = projeto.app.consumer_secret
    access_token = projeto.app.access_token
    access_secret = projeto.app.access_secret

    #Create a twitter API connection OAth.

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

    #Open/Create json append data
    data = open('data.json', 'a')
    f = json.dumps(data)



def search(projeto):
    try:
        api = connect(projeto)
    except:
        raise
    query = api.search(q="globoesporte", count=1, since=None)
    list_tweets = []
    for result in query:
        obj_tweet = result._json
        list_tweets.append(obj_tweet)
        print(json.dumps(list_tweets))
        # print(result["created_at"], result["user"]["screen_name"], result["text"])


def user(self, user_name):
    users = []
    for user in users:
        # print(users)
        user = tweepy.api.get_user(screen_name=user_name, count=1)
        f.write([user.screen_name, user.id, user.description.encode('uft-8')])
        print(user.id)
