__author__ = 'skuli'
from twython import Twython, TwythonError
import sqlite3 as lite
from authentication import auth

twitter = auth()
#followids1 = twitter.get_followers_ids(screen_name='HillaryClinton')
#response = twitter.get_followers_ids(screen_name = "HillaryClinton")
con = None


con = lite.connect('../test.db')
cur = con.cursor()


twittercursor = None
list1 = []
list2 = []

response = twitter.get_followers_ids(screen_name = "HillaryClinton")
twittercursor = response["next_cursor"]

while twittercursor:

    for i in response["ids"]:
        cur.execute("INSERT INTO users(twitter_id) VALUES(" + str(i) + ")")
        con.commit()

    response = twitter.get_followers_ids(screen_name = "HillaryClinton",cursor = twittercursor)
    twittercursor = response["next_cursor"]


#for x in response["ids"]:
#    print "numer 1:" +  str(x)
#    list1.append(x)

#response2 = twitter.get_followers_ids(screen_name = "HillaryClinton",cursor = response["next_cursor"])
#print "skuli"

#for y in response2["ids"]:
#    print "numer 2: " + str(y)
#    list2.append(y)

#interse = set(list1).intersection(list2)
#print interse

con.commit()

con.close()