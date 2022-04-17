from os import access
import tweepy
import configparser
import pandas as pd


#read credentials from config file
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# print(api_key)


#autenticate account/app to twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()

columns = ['Time', 'User', 'Tweet']
data = []

for tweet in public_tweets:
     data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
    # print(tweet.text)

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')
