__author__ = 'skuli'

from twython import Twython, TwythonError
import sqlite3 as lite
import time
from authentication import auth


def hugeSqlCommand(minFriendlyFollowing, maxOpponentFollowing, Friendlyparty, OpponentParty):
    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()

    cur.execute("SELECT users_following_politicians.users_id "
                "FROM users_following_politicians "
                "INNER JOIN politicians "
                "ON users_following_politicians.politicians_id = politicians.id "
                "WHERE politicians.party = '" + Friendlyparty + "' "
                "GROUP BY users_following_politicians.users_id "
                "HAVING (COUNT(users_following_politicians.users_id) > " + str(minFriendlyFollowing) + ") "
                "INTERSECT "
                "SELECT users_following_politicians.users_id "
                "FROM users_following_politicians "
                "INNER JOIN politicians "
                "ON users_following_politicians.politicians_id = politicians.id "
                "WHERE politicians.party = '" + OpponentParty + "' "
                "GROUP BY users_following_politicians.users_id "
                "HAVING (COUNT(users_following_politicians.users_id) < " + str(maxOpponentFollowing) + ");")

    users = cur.fetchall()
    cur2 = con.cursor()

    for u in users:
        print u[0]
        cur2.execute("insert into final_users (users_id, party) values (?, ?)",(u[0], Friendlyparty))

    con.commit()


def sortUsers(minFriendlyFollowing, maxOpponentFollowing):

    hugeSqlCommand(minFriendlyFollowing, maxOpponentFollowing, 'R', 'D')
    hugeSqlCommand(minFriendlyFollowing, maxOpponentFollowing, 'D', 'R')


def putUsersInTable(twitter):
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
                print "retry successful!"
            except:
                time.sleep(10)
                print "retrying..."
                continue
            break

        twittercursor = response["next_cursor"]

        while twittercursor:
            twittercursor = response["next_cursor"]

            for x in response["ids"]:
                cur.execute("SELECT id FROM users WHERE twitter_id = " + str(x))
                userid = cur.fetchall()
                if not userid:
                    cur.execute("INSERT INTO users(twitter_id) VALUES(" + str(x) + ")")
                    cur.execute("SELECT id FROM users WHERE twitter_id = " + str(x))
                    userid = cur.fetchall()
                    cur.execute("insert into users_following_politicians (users_id, politicians_id) values (?, ?)",(str(userid[0][0]), str(i[0])))
                else:
                    cur.execute("insert into users_following_politicians (users_id, politicians_id) values (?, ?)",(str(userid[0][0]), str(i[0])))


            con.commit()
            while True:
                try:
                    response = twitter.get_followers_ids(screen_name = i[2],cursor = twittercursor)
                    print "retry successful!"
                except:
                    time.sleep(10)
                    print "retrying..."
                    continue
                break

        con.commit()

    con.close()