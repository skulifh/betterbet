# -*- coding: utf-8 -*-
from better.CheckSpelling import SpellChecker
from better.languagechecker import checklang

__author__ = 'Asgeir'

from twython import Twython, TwythonError
from authentication import auth
from wordsindb import wordsindb
import sqlite3 as lite
import enchant
import re

def statuses():


    DesiredR = 100 #The number of English speaking Democrats desired
    DesiredD = 100 #The number of English speaking Republicans desired

    dict = enchant.Dict("en_US")
    twitter = auth()

    lineslist = [] #list for all the lines in the txt file
    wordslist = [] #list for all the words in the txt file

    Dcount = 0
    Rcount = 0

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur.execute("SELECT users_id, party FROM final_users")

    rows = cur.fetchall()

    print rows

    for IDs in rows:

        party = IDs[1]
        if party == "D" and Dcount >= DesiredD:
            continue
        if party == "R" and Rcount >= DesiredR:
            continue

        if Dcount == "D" and Rcount == "R":
            print "Done!"
            SpellChecker()
            break

        lineslist[:] = []
        wordslist[:] = []
        try:
            print str(IDs[0])
            user_timeline = twitter.get_user_timeline(id=str(IDs[0]), count=10)
            print user_timeline
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
        print "HOHOHO" + liststr
      #  wordsindb(IDs, liststr)
        print "PARTY " + str(IDs[1])
        partycounter = checklang(IDs[0], liststr, IDs[1])

        if partycounter == "D":
            Dcount += 1
        elif partycounter == "R":
            Rcount += 1

        if partycounter == "R" or partycounter == "D":
            wordsindb(IDs, liststr)


statuses()