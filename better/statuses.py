""" docstring, enter some text here! """
# -*- coding: utf-8 -*-
__author__ = 'Asgeir'
from twython import TwythonError
import sqlite3 as lite
from guess_language import guessLanguage
import time
import re

def statuses(twitter):
    """ docstring, enter some text here! """
    desired_r = 50 #The number of English speaking Democrats desired
    desired_d = 50 #The number of English speaking Republicans desired

    lineslist = [] #list for all the lines in the txt file
    wordslist = [] #list for all the words in the txt file

    d_count = 0
    r_count = 0

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur.execute("SELECT users_id, party FROM final_users")

    rows = cur.fetchall()
    cur = con.cursor()

    for ids in rows:

        party = ids[1]

        if d_count >= desired_d and r_count >= desired_r:
            print "Done!"
            break
        elif (party == "D" and d_count >= desired_d) or (party == "R" and r_count >= desired_r):
            continue

        lineslist[:] = []
        wordslist[:] = []
        print "before"
        try:
            user_timeline = twitter.get_user_timeline(id=str(ids[0]), count=10)
        except TwythonError as error:
            print error.error_code
            print error
            if error.error_code == 401:
                continue
            if error.error_code == 429:
                while True:
                    try:
                        user_timeline = twitter.get_user_timeline(id=str(ids[0]), count=10)
                        print('retry successful!')
                    except:
                        print('retrying...')
                        time.sleep(60)
                        continue
                    break
        print "after"


        for tweet in user_timeline:
            status = tweet['text'].encode('utf-8')

            status = clean_status(status)
            lineslist.append(status)

        for i in lineslist: #loop through all the lines in the list
            words = i.split() #acquire all the words in the line in a list

            for j in words: #loop through the word list to add them to another list
                if j.find("...") <= 0:
                    wordslist.append(j)

        liststr = ""

        for word in wordslist:
            liststr += word + " "
    #    print "PARTY " + str(IDs[1])
        if guessLanguage(liststr) == "en":
            cur.execute("INSERT INTO final_users_en(users_id, party) VALUES(?, ?)", (str(ids[0]), str(ids[1])))
            cur.execute("INSERT INTO statuses(users_id, statuses) VALUES(?, ?)",(repr((ids[0])), repr(liststr)))
            if party == "D":
                d_count += 1
            elif party == "R":
                r_count += 1

    con.commit()
    con.close()
 
def clean_status(status):
    """ docstring, enter some text here! """

    status = re.sub(r'@\w+\s?', '', status) #Removes words that start with "@", i.e. the usernames
    status = re.sub(r'#\w+\s?', '', status) #Removes words that start with "#", i.e. hashtags

    status = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}  +   '
                    r'/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+'
                    r'(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', status) #Removes URLs from the status

    status = status.replace(",", "") #Removes , from the status
    status = status.replace(".", "") #Removes . from the status
    status = status.replace("?", "") #Removes ? from the status
    status = status.replace("!", "") #Removes ! from the status
    status = status.replace("/", "") #Removes / from the status
    status = status.replace("-", "") #Removes - from the status
    status = status.replace(":", "") #Removes : from the status
    status = status.replace(";", "") #Removes ; from the status
    status = status.replace("“", "") #Removes “ from the status
    status = status.replace("”", "") #Removes ” from the status
    status = status.replace("(", "") #Removes ( from the status
    status = status.replace(")", "") #Removes ) from the status
    status = status.replace("\"", "") #Removes " from the status
    status = status.replace("'", "") #Removes ' from the status
    status = status.replace("@", "") #Removes @ from the status
    status = status.replace("\xe2\x80\x93", "") #Removes \xe2\x80\x93 from the status
    status = status.replace("\xe2\x80\xa6", "") #Removes \xe2\x80\xa6 from the status
    status = status.replace("\xe2\x80\x99", "") #Removes \xe2\x80\x99 from the status
    status = status.replace("%", "") #Removes % from the status
    #ADD EVERYTHING ON KEYBOARD NUMBERS

    return status