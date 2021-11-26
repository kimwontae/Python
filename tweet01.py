import tweepy
from tweepy import tweet
from tweepy.api import API

def connect_api():
    consumer_key = 'qdbEUoaBrr54j81FuXoCSjTaG'
    consumer_secret= 'NqmkGfzTs5EXq7zPeGMX9DfRFTPulYQmVJjeajL0VKjqfWOyo9'

    access_token ='1464064838389272577-ng4KyPmQEILWEgr07ULdEPtRwIDW53'
    access_secret = 'XDipZfQqXROCksGvfjSq1JEtBTR0xqTgZ5V8VxrTqH17I'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    return api
print(connect_api())


def get_tweets(api, username):
    tweets = api.user_timeline('bts_official')
    return tweets

api = connect_api()
#bts_timeline=get_tweets(api, 'bts_official')
print(get_tweets)
#tweet_update_status=api.update_status('eded')
#api.update_status(tweet)
#twee="exex"
#print("name:",api.me().name)


