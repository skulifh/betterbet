""" has the function huge_sql_command, sort_users and put_users_in_table """
__author__ = 'skuli'

import sqlite3 as lite
import time
import logging


def huge_sql_command(min_friendly_following, max_opponent_following, friendly_party, opponent_party):
    """ Runs one SQL command. Is in a special function due to being run more than once """
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    #global console

    cur.execute("SELECT users_following_politicians.twitter_id "
                "FROM users_following_politicians "
                "INNER JOIN politicians "
                "ON users_following_politicians.politicians_id = politicians.id "
                "WHERE politicians.party = '" + friendly_party + "' "
                "GROUP BY users_following_politicians.twitter_id "
                "HAVING (COUNT(users_following_politicians.twitter_id) >= " + str(min_friendly_following) + ") "
                "INTERSECT "
                "SELECT users_following_politicians.twitter_id "
                "FROM users_following_politicians "
                "INNER JOIN politicians "
                "ON users_following_politicians.politicians_id = politicians.id "
                "WHERE politicians.party = '" + opponent_party + "' "
                "GROUP BY users_following_politicians.twitter_id "
                "HAVING (COUNT(users_following_politicians.twitter_id) <= " + str(max_opponent_following) + ");")

    users = cur.fetchall()
    cur2 = con.cursor()

    for user in users:
        cur2.execute("insert into final_users (users_id, party) values (?, ?)",(user[0], friendly_party))

    con.commit()


def sort_users(min_friendly_following, max_opponent_following):
    """ Sort the users into eithere Democrats or Republicans """

    huge_sql_command(min_friendly_following, max_opponent_following, 'R', 'D')
    huge_sql_command(min_friendly_following, max_opponent_following, 'D', 'R')


def put_users_in_table(twitter):
    """ Gathers users from twitter who are following the politicians
     in the politicians database and puts them in the speciffic table"""
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()

    twittercursor = None

    cur.execute("SELECT * FROM politicians")
    rows = cur.fetchall()

    cur = con.cursor()

    for i in rows:
        while True:
            try:
                response = twitter.get_followers_ids(screen_name = i[2])
                logging.info('retry successful!')
            except:
                logging.info('retrying...')
                time.sleep(60)
                continue
            break

        twittercursor = response["next_cursor"]

        while twittercursor:
            twittercursor = response["next_cursor"]

            for twitter_id in response["ids"]:
                cur.execute("insert into users_following_politicians (twitter_id, politicians_id, party) values (?, ?, ?)",(str(twitter_id), str(i[0]), str(i[3])))

            con.commit()
            while True:
                try:
                    response = twitter.get_followers_ids(screen_name = i[2], cursor = twittercursor)
                    logging.info('retry successful!')
                except:
                    logging.info('retrying...')
                    time.sleep(60)
                    continue
                break

        con.commit()

    cur.execute("SELECT DISTINCT twitter_id FROM users_following_politicians")
    users_id = cur.fetchall()
    cur = con.cursor()

    for user_id in users_id:
        cur.execute("insert into users (id) values (?)",(str(user_id[0]),))

    con.commit()

    con.close()