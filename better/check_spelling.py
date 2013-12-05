""" docstring, enter some text here! """
__author__ = 'Asgeir'
import sqlite3 as lite
import enchant


def spell_checker():
    """ docstring, enter some text here! """

    dict_use = enchant.Dict("en_US")
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    cur2 = con.cursor()
    lines_list = []
    words_list = []
    party = "D" #Iniitializing the party as D

    d_correct_counter = 0
    d_incorrect_counter = 0
    r_correct_counter = 0
    r_incorrect_counter = 0


    cur.execute("select distinct(statuses.statuses), final_users_en.party from statuses,final_users_en where statuses.users_id = final_users_en.users_id and statuses.id < 10") #get statuses from 1000 D and 1000 R

    while True:
        lines_list[:] = []
        words_list[:] = []
        row = cur.fetchone()

        if row == None:
            break

        status = row[0]
        party = row[1]
        lines_list.append(status)
        print "STATUS: " + str(status)

        for i in range(len(lines_list)): #loop through all the lines in the list
            words = lines_list[i].split() #acquire all the words in the line in a list

            for j in range(len(words)): #loop through the word list to add them to another list
                if words[j].find("...") <= 0:
                    words_list.append(words[j])


        for k in range(len(words_list)-1):
            print "\n"
            print words_list[k]
            spell_check = dict_use.check(words_list[k])
            spell_check = str(spell_check)
            print spell_check
            print "Party: " + str(party)
            if spell_check == "True":
                if party == "D":
                    d_correct_counter += 1
                    print "HO HO LOLOL"
                elif party == "R":
                    r_correct_counter += 1
            elif spell_check == "False":
                if party == "D":
                    d_incorrect_counter += 1
                elif party == "R":
                    r_incorrect_counter += 1
            else:
                print spell_check + " SOMETHING IS WRONG!" #Debug purposes


    print "DCorrectCounter = " + str(d_correct_counter)
    print "DIncorrectCounter = " + str(d_incorrect_counter)
    print "RCorrectCounter = " + str(d_correct_counter)
    print "RIncorrectCounter = " + str(r_incorrect_counter)

    cur2.execute("INSERT INTO results(party, correct, incorrect) VALUES(?, ?, ?)", ('D', d_correct_counter, d_incorrect_counter))
    cur2.execute("INSERT INTO results(party, correct, incorrect) VALUES(?, ?, ?)", ('R', r_correct_counter, r_incorrect_counter))
    con.commit()
    con.close()