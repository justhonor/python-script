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

    # Sep 1 find emails that exists in CA but not in VA
    ca_execute(Find_Emails)
    va_execute(Find_Emails)

    Emails_CA  = ca_cursor.fetchall()
    Emails_VA  = va_cursor.fetchall()

    # Get difference between two list
    #Emails = list(set(Emails_CA)-set(Emails_VA))
    Emails = [x for x in Emails_CA if x not in Emails_VA]
    
    # Sep 2  find all userids by Emails
    S_Emails = list_to_string(Emails)
    
    Find_Userids = 'SELECT user_id FROM zm_user WHERE email in %s '%S_Emails
    print "Find_Userids:\n",Find_Userids
    
    ca_execute(Find_Userids)
    UserIds_CA = ca_cursor.fetchall() 
    
    S_UserIds_CA = list_to_string(UserIds_CA)
    print "UserIDs_CA:\n",S_UserIds_CA

    # Sep 3 find all infomation from CA  by UseIds
    FindAll_From_user = 'select * from zm_user where user_id in %s'%S_UserIds_CA
    print "FindAll_From_User:\n",FindAll_From_user

    ca_execute(FindAll_From_user)
    row=[]
    while row is not None:
        row = ca_cursor.fetchone()
        print(row)
    

    ca_cursor.close()
    ca_con.close()

    va_cursor.close()
    va_con.close()

def ca_execute(sql):
    try:
        ca_cursor.execute(sql)
    except :
        print 'ca_cursor Find_Userids error'
        sys.exit()


def va_execute(sql):
    try:
        va_cursor.execute(sql)
    except :
        print 'va_cursor Find_Emails_VA error'
        sys.exit()


def list_to_string(list_1):
    string=''
    for e in list_1:
        s_tmp = str(e).replace("(u","").replace(")","")
        string = string + s_tmp

    return '(' + string[:-1] + ')'

if __name__ == "__main__":
    global ca_con,ca_cursor
    global va_con,va_cursor

    ca_con,ca_cursor=connect(CA_HOST,CA_PORT,CA_USER,CA_PASSWD,DB)
    va_con,va_cursor=connect(VA_HOST,VA_PORT,VA_USER,VA_PASSWD,DB)

    user_sync()

