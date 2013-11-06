__author__ = 'Asgeir'

from guess_language import guessLanguage
import sqlite3 as lite
from CheckSpelling import SpellChecker

def checklang():

    DesiredR = 5 #The number of English speaking Democrats desired
    DesiredD = 3 #The number of English speaking Republicans desired

    Dcount = 0 #English speaking Democrats counter
    Rcount = 0 #English speaking Republicans counter
    party = "D" #Initialize party as D
    StopOuterLoop = 0 #Variable that stops the outer loop when the desired number of D or R is not reached

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur2 = con.cursor()

    while Rcount < DesiredR and StopOuterLoop != 1:

        cur.execute("select statuses.id, statuses.statuses from statuses,users_following_count where statuses.id = users_following_count.users_id and users_following_count.party = ?;", party) #Get the users that are democrats or republicans (follows X many D/R)

        while True:
            if Dcount >= DesiredD:
                if party == "D":
                    party = "R"
                    break
            if Rcount >= DesiredR:
                break

            row = cur.fetchone()

            if row == None:
                StopOuterLoop = 1
                if Dcount < DesiredD:
                    print "The number of Democrats is less than desired. The program will now stop."
                elif Rcount < DesiredR:
                    print "The number of Republicans is less than desired. The program will now stop."
                break

            statuses = row[1]

            language = guessLanguage(statuses)
            ID = (row[0])
            #print language
            if language == "en":
                cur2.execute("INSERT INTO final_users(users_id,party) VALUES(?,?)", (ID,party))
                if party == "D":
                    Dcount += 1
                    print "Dcount: " + str(Dcount)
                else:
                    Rcount += 1
                    print "Rcount: " + str(Rcount)

        con.commit()
    con.close()

checklang()
SpellChecker()