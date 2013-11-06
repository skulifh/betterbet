# -*- coding: utf-8 -*-
__author__ = 'Asgeir'

from twython import Twython, TwythonError
from authentication import auth
from wordsindb import wordsindb
import sqlite3 as lite
import enchant
import re

def statuses():

    dict = enchant.Dict("en_US")
    twitter = auth()

    lineslist = [] #list for all the lines in the txt file
    wordslist = [] #list for all the words in the txt file

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM final_users") #Get the users that are democrats or republic

    rows = cur.fetchall()

    for IDs in rows:

        lineslist[:] = []
        wordslist[:] = []
        try:
            cur.execute("SELECT twitter_id FROM users where id = " + str(IDs[1]) + ";")
            user_timeline = twitter.get_user_timeline(id=str(cur.fetchall()[0][0]), count=10)
        except TwythonError as e:
            print e

        for tweet in user_timeline:
            #print tweet['user']['screen_name'].encode('utf-8')
            #print "IDs: " + str(IDs)
            status = tweet['text'].encode('utf-8')

            status = re.sub(r'@\w+\s?','',status) #Removes words that start with "@", i.e. the usernames
            status = re.sub(r'#\w+\s?','',status) #Removes words that start with "#", i.e. hashtags

            status = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}  +   '
                                    r'/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+'
                                    r'(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', status) #Removes URLs from the status
            status = status.replace(",", ""); #Removes , from the status
            status = status.replace(".", ""); #Removes . from the status
            status = status.replace("?", ""); #Removes ? from the status
            status = status.replace("!", ""); #Removes ! from the status
            status = status.replace("/", ""); #Removes / from the status
            status = status.replace("-", ""); #Removes - from the status
            status = status.replace(":", ""); #Removes : from the status
            status = status.replace(";", ""); #Removes ; from the status
            status = status.replace("“", ""); #Removes “ from the status
            status = status.replace("”", ""); #Removes ” from the status
            status = status.replace("(", ""); #Removes ( from the status
            status = status.replace(")", ""); #Removes ) from the status
            status = status.replace("\"", ""); #Removes " from the status
            lineslist.append(status)

        for i in range(len(lineslist)): #loop through all the lines in the list
            words = lineslist[i].split() #acquire all the words in the line in a list

            for j in range(len(words)): #loop through the word list to add them to another list
                if words[j].find("...") <= 0:
                    wordslist.append(words[j])

        liststr = ""
        for word in wordslist:
            liststr += word + " "

        wordsindb(IDs, liststr)




statuses()