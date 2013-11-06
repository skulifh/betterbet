# -*- coding: utf-8 -*-
__author__ = 'Asgeir'

import sqlite3 as lite

def wordsindb(IDs ,liststr):

    con = None
    con = lite.connect('../test.db')
    cur = con.cursor()
    IDs = repr((IDs[1]))
    liststr = repr(liststr)

    cur.execute("INSERT INTO statuses(id, statuses) VALUES(?,?)",(IDs,liststr))
    con.commit()