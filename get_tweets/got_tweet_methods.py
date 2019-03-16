import tweepy #https://github.com/tweepy/tweepy
import os

# Finds the positions of each start / end quote for line in api_keys.txt
def return_key_position_length(line: str):
    start_quote = line.find('"')
    end_quote = line.find('"', start_quote + 1)
    return start_quote + 1, end_quote

# Returns the index start:end where the key string is located on the line
def return_key_from_line(line: str):
    start_pos, end_pos = return_key_position_length(line)
    return line[start_pos:end_pos]

# Authenticate with Twitter API using the tweepy OAuth handler
def authenticate():
    # read keys from api_text if available, otherwise use explicit definition below (do not share keys this way)
    # Twitter API credentials
    # Add keys below to api_keys.txt to read from file or complete variable assignment
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""

    try:  # Read the api keys from api_keys.txt unless not found
        api_key_file = open('api_keys.txt', 'r')
        lines = api_key_file.readlines()
        consumer_key = return_key_from_line(lines[0])
        consumer_secret = return_key_from_line(lines[1])
        access_key = return_key_from_line(lines[2])
        access_secret = return_key_from_line(lines[3])
        api_key_file.close()
    except FileNotFoundError:  # Error message
        print("api_keys.txt not found in " + os.path.join(os.path.dirname(__file__), '..'))

    # Authentication through Twitter OAuth via Tweepy (https://developer.twitter.com/en/docs)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)  # Twitter API object, used to make calls to the Twitter service
    return api


def return_tweets(twitter_handle):
    api = authenticate()  # returns the authenticated object tweepy.API(auth)
    # TODO: Add error handler if Twitter Handle account is private and returns request error
    tweets = api.user_timeline(twitter_handle, tweet_mode="extended")  # returns JSON obj containing tweets / meta data
    return tweets


