#!/usr/bin/python
# coding:utf-8
##
# Filename: t.py
# Author  : zane
# Date    : 2017-02-15
# Describe:
##
#############################################

import mysql.connector as connector
import sys

DB='ssbdb'
# Va mater
VA_HOST='datasyncva.co16f7xzvs0r.us-east-1.rds.amazonaws.com'
VA_DATABASE='RingCentralDB'
VA_USER='devdb'
VA_PASSWD='00000000'
VA_PORT='3306'

e=[(u'freeman16122211@mailinator.com',),(u'freeman1612221701@mailinator.com',),(u'free-with-account@mailinator.com',),(u'freeman16122208@mailinator.com',)]

s=''
st=''
print e

for ee in e:
    global s
    print "ee:",ee
    st = str(ee).replace("(u","").replace(")","")
    print "stt:",st
    s=s+st

s='('+s[:-1]+')'


#i=[(u'0XGZ2--TQPK7VO6QSIFGsQ', u'wGB-KJruSpOsyG6gIO9_Ng', 0, 2, None, 0, 16, 1, 0, u'freeman16122211@mailinator.com', 0, datetime.datetime(2016, 12, 23, 6, 12, 57), datetime.datetime(2016, 12, 23, 6, 18, 59), 0),(u'YUeb8YMGTXqS9uGK6l09Ww', u'kyKNM3sASRGYkk0LsoMBgQ', 0, 1, None, 0, 0, 0, 0, u'free-with-account@mailinator.com', None, datetime.datetime(2016, 12, 25, 3, 54, 47), datetime.datetime(2016, 12, 25, 4, 24, 29), 0)]

def connect(Host,Port,User,Passwd,Database):
    try:
        con = connector.connect(host=Host,port=Port,user=User,passwd=Passwd,database=Database)
    except Exception,e:
        print "connect to %s error\n"%Host,e
        sys.exit()

    cursor = con.cursor()
    return con,cursor

s="(u'YUeb8YMGTXqS9uGK6l09Ww', u'kyKNM3sASRGYkk0LsoMBgQ', 0, 1, None, 0, 0, 0, 0, u'free-with-account@mailinator.com', None, datetime.datetime(2016, 12, 25, 3, 54, 47), datetime.datetime(2016, 12, 25, 4, 24, 29), 0)"
insert='insert into zm_user vaules(%s)'%s
va_con,va_cursor=connect(VA_HOST,VA_PORT,VA_USER,VA_PASSWD,DB)
try:
    va_cursor.execute()
except:
    print "error!!"
    sys.exit()


