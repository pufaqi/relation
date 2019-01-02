#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:loftybay
import pymysql
db = pymysql.connect("47.75.111.127","pufaqi","pufaqi999,.QAZ","pytest")
cursor = db.cursor ()
sql = """
    #create table passwd (id int ,passwd INT )
    drop table passwd
"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()



