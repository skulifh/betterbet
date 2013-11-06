__author__ = 'skuli'
from twython import Twython, TwythonError
import sqlite3 as lite
from users import putUsersInTable
from authentication import auth

twitter = auth()
putUsersInTable(twitter)



#followids1 = twitter.get_followers_ids(screen_name='HillaryClinton')
#response = twitter.get_followers_ids(screen_name = "HillaryClinton")



