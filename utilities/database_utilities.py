import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'tweets.db')


# Create database to store tweets for different Twitter Handles and Semantics
def create_database(database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor() # connection cursor to SQL DB (Allows Python code to execute command in a database session)
        cur.execute("drop table if exists tweets")  # delete table to refresh for new tweets
        ddl = """CREATE TABLE tweets (handle,
        tweet_text TEXT, created_at TEXT, polarity REAL )"""  # Data Definition Language(DDL) for creating table (SQL)
        cur.execute(ddl)  # executes the DDL
    conn.close()


# Saves tweets (list) to the database including meta information
def save_tweets_to_database(tweet_list: list, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO tweets(handle, tweet_text, created_at, polarity) " \
              "VALUES(?, ?, ?, ?)"
        cur.execute(sql, tweet_list)


# Execute a SQL statement against created database e.g. sql = "SELECT * FROM db"
def execute_query(sql: str, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()  # fetchall returns records retrieved with SQL statement
