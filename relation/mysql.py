#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:pufaqi
#loftybay@163.com
import pymysql
db = pymysql.connect("47.75.111.127","root","pufaqi999,.QAZ","pytest")
cursor = db.cursor ()
sql = """
    create table abd(id int,username int)
"""
print("niuhao")
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close