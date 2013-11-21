__author__ = 'Asgeir'

from guess_language import guessLanguage
import sqlite3 as lite
from CheckSpelling import SpellChecker

def checklang(IDs ,liststr, party):

    DesiredR = 10 #The number of English speaking Democrats desired
    DesiredD = 10 #The number of English speaking Republicans desired

    Dcount = 0 #English speaking Democrats counter
    Rcount = 0 #English speaking Republicans counter
   #party = "" #Initialize party as D
    StopOuterLoop = 0 #Variable that stops the outer loop when the desired number of D or R is not reached

    partycounter = ""

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur2 = con.cursor()

    #while Rcount < DesiredR and StopOuterLoop != 1:

    # cur.execute("select statuses.id, statuses.statuses from statuses,final_users where statuses.id = final_users.users_id and final_users.party = ?;", party) #Get the users that are democrats or republicans (follows X many D/R)

    #while True:
    #    if Dcount >= DesiredD:
    #        if party == "D":
    #            party = "R"
    #            break
    #    if Rcount >= DesiredR:
    #        break

    #      row = cur.fetchone()

    #if row == None:
    #    StopOuterLoop = 1
    #    if Dcount < DesiredD:
    #        print "The number of Democrats is less than desired. The program will now stop."
    #    elif Rcount < DesiredR:
    #        print "The number of Republicans is less than desired. The program will now stop."
    #    break

    #  statuses = row[1]
    statuses = liststr
    print statuses

    language = guessLanguage(statuses)
    # ID = (row[0])
    #print language
    if language == "en":
        cur2.execute("INSERT INTO final_users_en(users_id,party) VALUES(?,?)", (str(IDs),str(party)))
        if party == "D":
            partycounter = "D"
            #   Dcount += 1
            #   print "Dcount: " + str(Dcount)
        else:
            partycounter = "R"
            #   Rcount += 1
            #   print "Rcount: " + str(Rcount)

    con.commit()
    con.close()
    return partycounter




#checklang()
