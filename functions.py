import tweepy
from tweepy import OAuthHandler, auth
from time import sleep
import json


def connect(projeto):
    consumer_key = projeto.app.consumer_key
    consumer_secret = projeto.app.consumer_secret
    access_token = projeto.app.access_token
    access_secret = projeto.app.access_secret

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    auth.secure = True
    api = tweepy.API(auth)
    myBot = api.get_user(screen_name='@mariana79664149')
    api.create_list(name="Desculpe adicionei voce", mode="public", description="Desculpe :(")
    return api

    def search(projeto):
        try:
            api = connect(projeto)
        except:
            raise

        # results = api.search(q='#ge', count=10)
        results = api.search(q='#apple', count=10)
        # list_tweets = []
        # for result in results:
        #     obj_tweet = json.dumps(result.entities)
        #     list_tweets.append(obj_tweet)
        #
        # print(list_tweets)

        for tweet in tweepy.Cursor(results, lang='en').items(10):
            try:
                if tweet.user.id == myBot.id:
                    continue
                print("\n\nTestando tweet  by: @" + tweet.user.screen_name)
                if (tweet.retweeted == False) or (tweet.favorited == False):
                    tweet.retweet()
                    tweet.favorite()
                    print("Resolvido")

                if tweet.user.follwing == False:
                    tweet.user.follow()
                    print(tweet)
                    print("Followed the user")

            except tweepy.TweepError as e:
                print(e.reason)
                sleep(10)
                continue
            except StopIteration:
                break


                # Process a single status
                # print(status._json)
