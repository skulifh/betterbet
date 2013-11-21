__author__ = 'Asgeir'
import sqlite3 as lite
import enchant


def SpellChecker():

    dict = enchant.Dict("en_US")
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur2 = con.cursor()
    lineslist = []
    wordslist = []
    party = "D" #Iniitializing the party as D
    StopOuterLoop = 0

    CorrectCounter = 0
    IncorrectCounter = 0
    DCorrectCounter = 0
    DIncorrectCounter = 0
    RCorrectCounter = 0
    RIncorrectCounter = 0

    while StopOuterLoop != 1:

        cur.execute("select statuses.statuses from statuses,final_users_en where statuses.id = final_users_en.users_id and final_users_en.party = ?", (party,)) #get statuses from 1000 D and 1000 R

        while True:

            lineslist[:] = []
            wordslist[:] = []

            row = cur.fetchone()
            #
            #if row == None:
            #    if party == "D":
            #        party = "R"
            #        DCorrectCounter = CorrectCounter
            #        DIncorrectCounter = IncorrectCounter
            #        CorrectCounter = 0
            #        IncorrectCounter = 0
            #        break
            #    elif party == "R":
            #        StopOuterLoop = 1
            #        RCorrectCounter = CorrectCounter
            #        RIncorrectCounter = IncorrectCounter
            #        CorrectCounter = 0
            #        IncorrectCounter = 0
            #        break


            statuses = row[0]

            lineslist.append(statuses)

            for i in range(len(lineslist)): #loop through all the lines in the list
                words = lineslist[i].split() #acquire all the words in the line in a list

                for j in range(len(words)): #loop through the word list to add them to another list
                    if words[j].find("...") <= 0:
                        wordslist.append(words[j])


            for k in range(len(wordslist)-1):
          #      print wordslist[k]
                spellcheck = dict.check(wordslist[k])
                spellcheck = str(spellcheck)
           #     print spellcheck
                if spellcheck is "True":
                    CorrectCounter += 1
                elif spellcheck is "False":
                    IncorrectCounter += 1
                else:
                    print spellcheck + " SOMETHING IS WRONG!" #Debug purposes


    print "DCorrectCounter = " + str(DCorrectCounter)
    print "DIncorrectCounter = " + str(DIncorrectCounter)
    print "RCorrectCounter = " + str(RCorrectCounter)
    print "RIncorrectCounter = " + str(RIncorrectCounter)

    cur2.execute("INSERT INTO results(party,correct,incorrect) VALUES(?,?,?)", ('D',DCorrectCounter,DIncorrectCounter));
    cur2.execute("INSERT INTO results(party,correct,incorrect) VALUES(?,?,?)", ('R',RCorrectCounter,RIncorrectCounter));
    con.commit()
    con.close()