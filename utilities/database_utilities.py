import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'words.db')


# Create database to store tweets for different Twitter Handles and Semantics
def create_database(database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = """CREATE TABLE tweets (handle TEXT PRIMARY KEY NOT NULL, 
        tweet_text TEXT, polarity INT NOT NULL )"""
        cur.execute(ddl)
    conn.close()

# Saves tweets to the database and
def save_tweets_to_database(tweet_list: list, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        for tweet in tweet_list:
            # check to see if the words is in there
            sql = "select count(word) from words where word='" + tweet + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cur.execute(sql)
        print("Database save complete!")

# Execute a SQL statement against created database
def execute_query(sql: str, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
