# main module
from textblob import TextBlob
from utilities import database_utilities
from get_tweets import got_tweet_methods
import ctypes
import os

# Loop through Twitter handles in text file, pass to Twitter API, and return values for storage in db
def main():
    database_utilities.create_database()  # Creates the database

    # Open the file with twitter handles to query tweets
    twitter_handles_file = open('handles.txt', 'r')
    try:
        lines = twitter_handles_file.readlines()  # read the lines in handles.txt
    except:
        print("handles.txt not found in " + os.path.join(os.path.dirname(__file__), '..'))

    # Saves Tweets to database, retrieving tweets (via API) from handle 1 at a time
    for handle in lines:
        tweets = got_tweet_methods.return_tweets(handle)  # return list of tweets from handle
        # print(tweets)
        for tweet in tweets:
            b = TextBlob(tweet.full_text)  # return TextBlob semantic info for individual tweet string
            tweet_list = [handle, tweet.full_text, tweet.created_at, b.sentiment[0]]  # save attributes to list
            database_utilities.save_tweets_to_database(tweet_list)  # insert list into database as row
        print(handle + " records saved to database")


if __name__ == "__main__":
    main()
    print("End of program")
    ctypes.windll.user32.MessageBoxW(0, "Tweets saved to database", "Tweet Semantics", 1)  # windows message box


