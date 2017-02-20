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
#import ipdb

START_TIME="'2016-12-20'"
END_TIME="'2016-12-22'"

DB='ssbdb'

# Ca slave could write
CA_HOST='datasyncca.cx8segvsabtq.us-west-1.rds.amazonaws.com'
CA_USER='devdb'
CA_PASSWD='00000000'
CA_PORT='3306'

# Va mater
VA_HOST='datasyncva.co16f7xzvs0r.us-east-1.rds.amazonaws.com'
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
    #print "Emails_CA:\n",Emails_CA
    #print "Emails_VA:\n",Emails_VA

    # Get difference between two list
    Emails = list(set(Emails_CA)-set(Emails_VA))
    #Emails = [x for x in Emails_CA if x not in Emails_VA]
    #print "Emails %s"%Emails 
    if Emails == []:
        print "There are no different between CA and VA on zm_user"
        sys.exit()
    # Sep 2  find all userids by Emails
    S_Emails = list_to_string(Emails)
    
    Find_Userids = 'SELECT user_id FROM zm_user WHERE email in %s '%S_Emails
    #print "Find_Userids:\n",Find_Userids
    
    ca_execute(Find_Userids)
    UserIds_CA = ca_cursor.fetchall() 
    
    S_UserIds_CA = list_to_string(UserIds_CA)
    #print "UserIDs_CA:\n",S_UserIds_CA

    # Sep 3 find all infomation from CA  by UseIds
    FindAll_From_user = 'select * from zm_user where user_id in %s'%S_UserIds_CA
    FindAll_From_usersns = 'select * from zm_usersns where user_id in %s'%S_UserIds_CA
    FindAll_From_userprofile = 'select * from zm_userprofile where user_id in %s'%S_UserIds_CA
    print "FindAll_From_User:\n",FindAll_From_user
    print "FindAll_From_Usersns:\n",FindAll_From_usersns
    print "FindAll_From_Userprofile:\n",FindAll_From_userprofile

    ca_execute(FindAll_From_user)
    All_From_user=ca_cursor.fetchall()

    ca_execute(FindAll_From_usersns)
    All_From_usersns=ca_cursor.fetchall()

    ca_execute(FindAll_From_userprofile)
    All_From_userprofile=ca_cursor.fetchall()
    #print "All_From_user:\n",All_From_user
    #print "All_From_usersns:\n",All_From_usersns
    #print "All_From_userprofile:\n",All_From_userprofile

    # Sep 4 insert into all infomation from CA to VA
    insert_all_user = 'insert ignore into zm_user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_all_usersns = 'insert ignore into zm_usersns values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_all_userprofile = 'insert ignore into zm_userprofile values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    excutemany("va",insert_all_user,All_From_user)
    excutemany("va",insert_all_usersns,All_From_usersns)
    excutemany("va",insert_all_userprofile,All_From_userprofile)


# meeting sync
def meeting_sync():
    # Sep 1 find all meeting_numbers
    Find_meeting_numbers = "SELECT meeting_number FROM zm_meeting WHERE modify_time > %s AND modify_time < %s AND TYPE > 1 AND TYPE != 4 AND create_time > %s AND create_time < %s"%(START_TIME,END_TIME,START_TIME,END_TIME)
    print "Find_meeting_numbers:\n",Find_meeting_numbers
    ca_execute(Find_meeting_numbers)
    meeting_numbers=ca_cursor.fetchall()
    #print "meeting_numbers:\n",meeting_numbers
    s_meeting=''
    for num in meeting_numbers:
        s_t=str(num).replace("(","'").replace(",)","',")
        s_meeting=s_meeting+s_t
    s_meeting_numbers= s_meeting[:-1] 

    # Sep 2 find all information from zm_meeting_ext,zm_webinar_ext,zm_meeting 
    Find_all_from_meeting = "SELECT * FROM zm_meeting WHERE modify_time > %s AND modify_time < %s AND TYPE > 1 AND TYPE != 4 AND create_time > %s AND create_time < %s"%(START_TIME,END_TIME,START_TIME,END_TIME)
    Find_all_from_meetingext="SELECT * FROM zm_meeting_ext WHERE meeting_number IN (%s) AND mkey!='hybrid'"%s_meeting_numbers
    Find_all_from_webinar="SELECT * FROM `zm_webinar_ext` WHERE meeting_number IN (%s)"%s_meeting_numbers
    
    #print "Find_all_from_meetingext:\n",Find_all_from_meetingext
    #print "Find_all_from_webinar:\n",Find_all_from_webinar

    ca_execute(Find_all_from_meeting)
    all_from_meeting=ca_cursor.fetchall()
    print "all_from_meeting:\n",all_from_meeting
    
    ca_execute(Find_all_from_meetingext)
    all_from_meetingext=ca_cursor.fetchall()
    print "all_from_meetingext:\n",all_from_meetingext
    
    ca_execute(Find_all_from_webinar)
    all_from_webinar=ca_cursor.fetchall()
    print "all_from_webinar:\n",all_from_webinar

    # Sep 3 find all information from zm_webinar_user
    Find_all_from_webinar_user="SELECT * FROM `zm_webinar_user` WHERE create_time > %s AND create_time < %s"%(START_TIME,END_TIME)

    ca_execute(Find_all_from_webinar_user)
    all_from_webinar_user=ca_cursor.fetchall()
    print "all_from_webinar_user:\n",all_from_webinar_user

    # Sep 4 insert into all information from CA to VA
    insert_all_meeting = 'insert ignore into zm_meeting values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_all_meetingext = 'insert ignore into zm_meeting_ext values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_all_webinarext = 'insert ignore into zm_webinar_ext values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_all_webinaruser = 'insert ignore into zm_webinar_user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    excutemany("va",insert_all_meeting,all_from_meeting)
    excutemany("va",insert_all_meetingext,all_from_meetingext)
    excutemany("va",insert_all_webinarext,all_from_webinar)
    excutemany("va",insert_all_webinaruser,all_from_webinar_user)

# telephone usage sync
def tel_sync():
    # Sep 1 find all information from CA zm_tel_call
    Find_all_from_tel='SELECT * FROM zm_tel_call WHERE create_time > %s AND create_time < %s'%(START_TIME,END_TIME)
    print "Find_all_from_tel:\n",Find_all_from_tel

    ca_execute(Find_all_from_tel)
    all_from_tel=ca_cursor.fetchall()
    print "all_from_tel:\n",all_from_tel

    # Sep 2 insert ignore into all information from CA to VA
    insert_all_tel ='insert ignore into zm_tel_call values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    excutemany("va",insert_all_tel,all_from_tel)

# account sync  --related tables(zm_account,zm_account_subscription)
def account_sync():
    '''
        zm_account 
    '''
    # Sep 1 find account_ids that from ca but not exists va
    Find_account_ids='SELECT account_id FROM zm_account WHERE create_time > %s AND create_time < %s'%(START_TIME,END_TIME)
    print "Find_account_ids:\n",Find_account_ids

    ca_execute(Find_account_ids)
    ca_account_ids=ca_cursor.fetchall()
    #print "ca_account_ids:\n",ca_account_ids

    va_execute(Find_account_ids)
    va_account_ids=va_cursor.fetchall()
    #print "va_account_ids:\n",va_account_ids

    # Get difference betweent above two list
    account_ids=[x for x in ca_account_ids if x not in va_account_ids ]
    print "account_ids:\n",account_ids
    if account_ids == []:
        print "There are no different between CA and VA on zm_account"
        sys.exit()

    S_account_ids=list_to_string(account_ids)
    print "s_account_ids:\n",S_account_ids

    # Sep 2 find all information from ca using above accout_ids.
    Find_all_from_account='select * from zm_account where account_id in %s'%S_account_ids

    ca_execute(Find_all_from_account)
    ca_all_from_account=ca_cursor.fetchall()

    # Sep 3 insert ignore all information that found above from ca to va
    # there are 96 columns in table zm_account,need 96 %s
    insert_all_from_account='insert ignore into zm_account values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    excutemany("va",insert_all_from_account,ca_all_from_account)

    '''
        zm_account_subscription
    '''
    # Sep 1 find all information from CA zm_tel_call
    Find_all_from_sub='SELECT * FROM zm_account_subscription WHERE create_time > %s AND create_time < %s'%(START_TIME,END_TIME)
    print "Find_all_from_sub:\n",Find_all_from_sub

    ca_execute(Find_all_from_sub)
    all_from_sub=ca_cursor.fetchall()
    print "all_from_sub:\n",all_from_sub

    # Sep 2 insert ignore into all information from CA to VA
    insert_all_sub ='insert ignore into zm_tel_call values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    excutemany("va",insert_all_sub,all_from_sub)
    
# zm_account compare one by one using modify_time
'''
    If any column in zm_account's rows are different betweent CA and VA.And VA modify_time earlier than CA.Update the row from ca to va.
'''
def account_comp():
    # Sep 1 get all from ca and va using modify_time
    Get_all='SELECT * FROM zm_account WHERE modify_time > %s AND modify_time < %s'%(START_TIME,END_TIME)
    print "Get_all:\n",Get_all


    ca_execute(Get_all)
    ca_get_all=ca_cursor.fetchall()
    #print "ca_get_all:\n",ca_get_all


    va_execute(Get_all)
    va_get_all=va_cursor.fetchall()
    #print "va_get_all:\n",va_get_all
    

    # Sep 2 compare modify_time and column
    length=len(ca_get_all)
    if length != len(va_get_all):
        print "account error!"
        sys.exit()

    other_ca = ca_get_all
    other_va = va_get_all
    need_insert=[]
    # modify_time index is 93
    for i in range(length):
        #ipdb.set_trace()
        if ca_get_all[i][93] > va_get_all[i][93]:           # the va modify_time earlier than ca
            other_ca[i]=ca_get_all[i][0:93]+ca_get_all[i][94:]
            other_va[i]=va_get_all[i][0:93]+va_get_all[i][94:]
            if cmp(other_ca[i],other_va[i]) != 0 :          # there are some difference in other column 
                #print "update:\n",ca_get_all[i][0]
                delete="delete from zm_account where account_id = '%s'"%ca_get_all[i][0]
                print "delete:\n",delete
                #va_execute(delete)
                insert="insert ignore into zm_account values( '%s' )"%ca_get_all[i]
                print "insert:\n",insert
                #va_execute(insert)
     #          need_insert.append(ca_get_all[i])
            else:
                print "no different betweent other column\n"

        else:
            print "ca_modify_time:%s   va_modify_time:%s"%(ca_get_all[i][93],va_get_all[i][93])
    #print "need_insert:\n",need_insert
    #insert='insert ignore into zm_account values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #excutemany("va",insert,need_insert)





def excutemany(location,sql,vaules):
    if location == "ca":
        try:
            ca_cursor.executemany(sql,vaules)
        except Exception,e:
            print "ca_cursor executemany error:",e
            sys.exit()
    elif location == "va":
        try:
            va_cursor.executemany(sql,vaules)
            va_con.commit()
        except Exception,e:
            print "va_cursor executemany error:",e
            sys.exit()
    else:
        print "no such location"
        sys.exit()

def ca_execute(sql):
    try:
        ca_cursor.execute(sql)
    except :
        print "ca_cursor sql:%s error"%sql
        sys.exit()

def va_execute(sql):
    try:
        va_cursor.execute(sql)
    except :
        print 'va_cursor sql:%s error'%sql
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

    #meeting_sync()
    #user_sync()
    #tel_sync()
    #account_sync()
    account_comp()

    ca_cursor.close()
    ca_con.close()

    va_cursor.close()
    va_con.close()
