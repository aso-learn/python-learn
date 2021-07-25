#! /usr/bin/env python3
# coding:utf-8
import pymysql
db = pymysql.connect(host="localhost",user="root",passwd="123456",db="quan")

cursor = db.cursor()

cursor.execute("SELECT * FROM people;")
a=cursor.fetchall()
for x in a:
    print(x)

