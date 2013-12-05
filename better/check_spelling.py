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

    d_correct_counter = 0
    d_incorrect_counter = 0
    r_correct_counter = 0
    r_incorrect_counter = 0

    d_count = 0
    r_count = 0

    cur.execute("select statuses.statuses, final_users_en.party from statuses,"
                "final_users_en where statuses.users_id = "
                "final_users_en.users_id") #get statuses from 1000 D and 1000 R

    while True:

        lines_list[:] = []
        words_list[:] = []
        row = cur.fetchone()

        if row == None:
            break

        status = row[0]
        party = row[1]

        if party == "D":
            d_count += 1
        elif party == "R":
            r_count += 1

        print "STATUS: " + str(status)

        words = status.split()
        for word in words:
            words_list.append(word)

        for k in words_list:
            print "\n"
            print k
            spell_check = dict_use.check(k)
            spell_check = str(spell_check)
            print spell_check
            print "Party: " + str(party)

            if spell_check == "True":
                if party == "D":
                    d_correct_counter += 1
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

    cur2.execute("INSERT INTO results(party, correct, incorrect) "
                 "VALUES(?, ?, ?)",
                 ('D', d_correct_counter, d_incorrect_counter))
    cur2.execute("INSERT INTO results(party, correct, incorrect) "
                 "VALUES(?, ?, ?)",
                 ('R', r_correct_counter, r_incorrect_counter))
    con.commit()
    con.close()