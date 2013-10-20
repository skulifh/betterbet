__author__ = 'skuli'

from twython import Twython, TwythonError
import sqlite3 as lite
from authentication import auth

def putUsersInTable(screenname, twitter):
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()

    twittercursor = None

    response = twitter.get_followers_ids(screen_name = screenname)

    while twittercursor:
        twittercursor = response["next_cursor"]

        for i in response["ids"]:
            cur.execute("INSERT INTO users(twitter_id) VALUES(" + str(i) + ")")

        con.commit()
        response = twitter.get_followers_ids(screen_name = screenname,cursor = twittercursor)

    con.commit()

    con.close()