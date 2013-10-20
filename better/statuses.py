# -*- coding: utf-8 -*-
__author__ = 'Asgeir'

from twython import Twython, TwythonError
from authentication import auth
import sqlite3 as lite
import enchant
import re

def statuses():

    dict = enchant.Dict("en_US")

    twitter = auth()

    lineslist = [] #list for all the lines in the txt file
    wordslist = [] #list for all the words in the txt file
    idlist = [] #List for IDs

    con = None


    con = lite.connect('../test.db')
    cur = con.cursor()

    #con = lite.connect('testy.db')
    #
    #with con:
    #    cur = con.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    print rows

    for IDs in rows:
        try:
            user_timeline = twitter.get_user_timeline(id=str(IDs[1]), count=10)
        except TwythonError as e:
            print e

        for tweet in user_timeline:
            print tweet['user']['screen_name'].encode('utf-8')
            print "IDs: " + str(IDs)
            status = tweet['text'].encode('utf-8')
            print status
            status = re.sub(r'@\w+\s?','',status) #Removes words that start with "@", i.e. the usernames
            status = re.sub(r'#\w+\s?','',status) #Removes words that start with "#", i.e. hashtags

            status = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}  +   '
                                    r'/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+'
                                    r'(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', status)
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

    CorrectCounter = 0
    IncorrectCounter = 0

    for k in range(len(wordslist)-1):
        spellcheck = dict.check(wordslist[k])
        spellcheck = str(spellcheck)
        if spellcheck is "True":
            CorrectCounter += 1
        elif spellcheck is "False":
            IncorrectCounter += 1
        else:
            print spellcheck + "LOLOLOLOLOLOLOLOLOLOLOLOL"

    #print wordslist[51]
    #print wordslist
    #print len(wordslist)
    print "TRUE = " + str(CorrectCounter)
    print "FALSE = " + str(IncorrectCounter)

statuses()