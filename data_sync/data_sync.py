#!/usr/bin/python
# coding:utf-8
##
# Filename: data_sync.py
# Author  : zane
# Date    : 2017-01-19
# Describe:
##
#############################################

import mysql.connector as connector
import sys


START_TIME="'2016-12-20'"
END_TIME="'2016-12-30'"

DB='ssbdb'

# Ca slave could write
CA_HOST='datasyncca.cx8segvsabtq.us-west-1.rds.amazonaws.com'
CA_DATABASE='RingCentralDB'
CA_USER='devdb'
CA_PASSWD='00000000'
CA_PORT='3306'

# Va mater
VP_HOST='datasyncva.co16f7xzvs0r.us-east-1.rds.amazonaws.com'
VP_DATABASE='RingCentralDB'
VP_USER='devdb'
VP_PASSWD='00000000'
VP_PORT='3306'

# Va slave readonly
VA_HOST='datasyncvaread.co16f7xzvs0r.us-east-1.rds.amazonaws.com'
VA_DATABASE='RingCentralDB'
VA_USER='devdb'
VA_PASSWD='00000000'
VA_PORT='3306'

def connect(Host,Port,User,Passwd,Database):
    try:
        con = connector.connect(host=Host,port=Port,user=User,passwd=Passwd,database=Database)
    except Exception,e:
        print "connect to %s error\n"%Host,e
        sys.exit()

    cursor = con.cursor()
    return con,cursor

# user sync
def user_sync():
    Find_Emails='SELECT DISTINCT email FROM zm_user WHERE create_time > %s AND create_time < %s '%(START_TIME,END_TIME)

    print 'Find_emails_ca:\n%s'%Find_Emails

    ca_con,ca_cursor=connect(CA_HOST,CA_PORT,CA_USER,CA_PASSWD,DB)
    va_con,va_cursor=connect(VA_HOST,VA_PORT,VA_USER,VA_PASSWD,DB)

    # Find emails that exists in CA but not in VA
    try:
        ca_cursor.execute(Find_Emails)
    except :
        print 'ca_cursor Find_Emails_CA error'
        sys.exit()

    try:
        va_cursor.execute(Find_Emails)
    except :
        print 'va_cursor Find_Emails_VA error'
        sys.exit()

    Emails_CA  = ca_cursor.fetchall()
    Emails_VA  = va_cursor.fetchall()

    #print "CA:\n",Emails_CA
    #print "VA:\n",Emails_VA

    # Get difference between two list
    #Emails = list(set(Emails_CA)-set(Emails_VA))
    Emails = [x for x in Emails_CA if x not in Emails_VA]

    #print Emails

    for email in Emails:
        print email
    # Find all userids by Emails
    Find_Userids='SELECT user_id FROM zm_user WHERE email in %s '%Emails
    try:
        ca_cursor.execute(Find_Userids)
    except :
        print 'ca_cursor Find_Userids error'
        sys.exit()

    UserIds_CA = ca_cursor.fetchall() 
    print UserIds_CA

    ca_cursor.close()
    ca_con.close()

    va_cursor.close()
    va_con.close()

user_sync()

