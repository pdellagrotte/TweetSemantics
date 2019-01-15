# main module
from textblob import TextBlob
from utilities import database_utilities
from get_tweets import got_tweet_methods

# Loop through Twitter handles in text file, pass to Twitter API, and return values for storage in db
def main():
    database_utilities.create_database()  # Creates the database

    # Open the file with twitter handles to query tweets
    twitter_handles_file = open('handles.txt', 'r')
    lines = twitter_handles_file.readlines()

    # Saves Tweets to database
    for handle in lines:
        tweets = got_tweet_methods.return_tweets(handle)
        # print(tweets)
        for tweet in tweets:
            b = TextBlob(tweet.full_text)
            tweet_list = [handle, tweet.full_text, tweet.created_at, b.sentiment[0]]
            database_utilities.save_tweets_to_database(tweet_list)
        print(handle + " records saved to database")
    print("End of program")

if __name__ == "__main__":
    main()

