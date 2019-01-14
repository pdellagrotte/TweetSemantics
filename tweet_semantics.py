# main module
from textblob import TextBlob
from get_tweets import got_tweet_methods


def main():
    # Open the file with twitter handles to query tweets
    twitter_handles_file = open('handles.txt', 'r')
    lines = twitter_handles_file.readlines()

    for handle in lines:
        tweets = got_tweet_methods.return_tweets(handle)
        # print(tweets)
        for tweet in tweets:
            print(handle, tweet.full_text)


    # Save tweets to database
    # TODO: Write code to save tweets to database

if __name__ == "__main__":
    main()

