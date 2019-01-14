from get_tweets import got_tweet_methods
import json
import pprint
import time

twitter_handles_file = open('handles.txt', 'r')
lines = twitter_handles_file.readlines()

for handle in lines:
    tweets = got_tweet_methods.return_tweets(handle)
    # print(tweets)
    for tweet in tweets:
        print(tweet.full_text)
        # time.sleep(1)