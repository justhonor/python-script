#!/usr/bin/python
# coding:utf-8
##
# Filename: monitor_PK.py
# Author  : zane
# Date    : 2017-02-22
# Describe:
##
#############################################

import mysql.connector as connector
import sys
#import ipdb

DB='ssbdb'

Theashold=1000

# Ca slave could write
CA_HOST='xxxx'
CA_USER='devdb'
CA_PASSWD='00000000'
CA_PORT='3306'

def connect(Host,Port,User,Passwd,Database):
    try:
        con = connector.connect(host=Host,port=Port,user=User,passwd=Passwd,database=Database)
    except Exception,e:
        print "connect to %s error\n"%Host,e
        sys.exit()

    cursor = con.cursor()
    return con,cursor

def ca_execute(sql):
    try:
        ca_cursor.execute(sql)
    except Exception,e:
        print "ca_cursor sql:%s error"%sql,e
        sys.exit()

# Distinguished tables with using Auto-increment INT as primary key or not
def DistTable():

    Auto_tables={}
    UnAuto_tables=[]
    
    TablesStatus='show table status;'
    ca_execute(TablesStatus)
    tables_status=ca_cursor.fetchall()
    
    #print "tabels_status:\n",tables_status
    table_numbers=len(tables_status)
    #ipdb.set_trace()
    for i in range(table_numbers):
        if tables_status[i][10] > 0:
            Auto_tables['%s'%tables_status[i][0]]=tables_status[i][10]
        else:
            UnAuto_tables.append(tables_status[i][0])

    #print "Auto_tables:\n",Auto_tables
    #print "UnAuto_tables:\n",UnAuto_tables
    return Auto_tables,UnAuto_tables

# Judege if the auto-increment is primary key or not 
def Is_Auto_PK(table):
    
    DESC="DESC %s"%table
    #ca_execute(Show_C_Table)
    ca_execute(DESC)
    table_info=ca_cursor.fetchall()

   # ipdb.set_trace()
   # print table_info
    
    rang=len(table_info)
    for i in range(rang):
        if table_info[i][3] == 'PRI' and table_info[i][5] == 'auto_increment':
            #print "%s Is_AUto_PK"%table
            return 1

    #print "%s Is not AUto_PK\n"%table
    return 0  
    #return PK_Auto_tables,PK_UnAuto_tables

if __name__ == "__main__":

    global ca_con,ca_cursor
    ca_con,ca_cursor=connect(CA_HOST,CA_PORT,CA_USER,CA_PASSWD,DB)

    Auto_tables,UnAuto_tables=DistTable()

    Over_threshold=[]
    for table in Auto_tables:
        #ipdb.set_trace()
        if not Is_Auto_PK(table):
            UnAuto_tables.append(table)
            continue
        else:
            if Auto_tables[table] > Theashold:
                Over_threshold.append(table)
                #print "Auto-increment is over 100m"

    print "There are some table do not use INT Auto_increment as it's PK:\n",UnAuto_tables
    print 
    print "The list of  tables which the value of PK over %s is :\n%s"%(Theashold,Over_threshold)
    ca_cursor.close()
    ca_con.close()
