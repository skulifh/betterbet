# -*- coding: utf-8 -*-

__author__ = 'Asgeir'

from twython import Twython, TwythonError
import sqlite3 as lite
from guess_language import guessLanguage
import enchant
import time
import re

def statuses(twitter):

    DesiredR = 100 #The number of English speaking Democrats desired
    DesiredD = 100 #The number of English speaking Republicans desired

    dict = enchant.Dict("en_US")

    lineslist = [] #list for all the lines in the txt file
    wordslist = [] #list for all the words in the txt file

    Dcount = 0
    Rcount = 0

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur.execute("SELECT users_id, party FROM final_users")

    rows = cur.fetchall()
    cur = con.cursor()

    for IDs in rows:

        party = IDs[1]

        if Dcount >= DesiredD and Rcount >= DesiredR:
            print "Done!"
            break
        elif (party == "D" and Dcount >= DesiredD) or (party == "R" and Rcount >= DesiredR):
            continue

        lineslist[:] = []
        wordslist[:] = []
        print "before"
        try:
            user_timeline = twitter.get_user_timeline(id=str(IDs[0]), count=10)
        except TwythonError as e:
            print e.error_code
            print e
            if e.error_code == 401:
                continue
            if e.error_code == 429:
                while True:
                    try:
                        user_timeline = twitter.get_user_timeline(id=str(IDs[0]), count=10)
                        print('retry successful!')
                    except:
                        print('retrying...')
                        time.sleep(60)
                        continue
                    break
        print "after"


        for tweet in user_timeline:
            status = tweet['text'].encode('utf-8')

            status = cleanStatus(status);
            lineslist.append(status)

        for i in lineslist: #loop through all the lines in the list
            words = i.split() #acquire all the words in the line in a list

            for j in words: #loop through the word list to add them to another list
                if j.find("...") <= 0:
                    wordslist.append(j)

        liststr = ""

        for word in wordslist:
            liststr += word + " "

        print "PARTY " + str(IDs[1])
        if guessLanguage(liststr) == "en":
            cur.execute("INSERT INTO final_users_en(users_id,party) VALUES(?,?)", (str(IDs[0]),str(IDs[1])))
            cur.execute("INSERT INTO statuses(users_id, statuses) VALUES(?,?)",(repr((IDs[0])),repr(liststr)))
            if party == "D":
                Dcount += 1
            elif party == "R":
                Rcount += 1

    con.commit()
    con.close()


def cleanStatus(status):

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
    return status