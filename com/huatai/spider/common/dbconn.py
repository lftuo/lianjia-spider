#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-11 14:53:06
# @File : dbconn.py
# @Software : PyCharm
# 数据库链接
import sqlite3
conn = sqlite3.connect('E:/tuotuo/dbdata/test.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS person (id integer PRIMARY KEY ,name varchar(20),age integer)')
data = "1,'qiye',20"
cur.execute(' INSERT INTO person VALUES (%s)'%data)
conn.commit()