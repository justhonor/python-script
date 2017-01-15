#!/usr/bin/python
# coding:utf-8
##
# Filename: login_notify.py
# Author  : zane
# Date    : 2017-01-13
# Describe:
##
#############################################

import subprocess as sub
import sys
#import ipdb
import time 

sys.path.insert(0,"send_mail")
import send_mail as send

USERS_INFO=[]
ToAddr = '541469923@qq.com'

def find_users():
    global USERS_INFO
    cmd = ['who']
    p = sub.Popen(cmd,stdout=sub.PIPE,stderr=sub.PIPE)
    out,err = p.communicate()
    
    if err != "":
        print err 
        sys.exit()

    outlines = out.splitlines()
    #print out
    #print outlines
    if USERS_INFO == []:
        for user_info in outlines:
            #print user_info
            #ipdb.set_trace()
            USERS_INFO.append(user_info)
        #print "[] send mail:%s"%out
        SendMail(out)
    else:
        report=''
        USERS_INFO_TMP = USERS_INFO
        
        #print USERS_INFO
        #print "this is out:%s"%out
        for user_info in outlines:
            need_append = 1 
            for user in USERS_INFO:
                #print user
                # IF the user_info exsits break
                #ipdb.set_trace()
                if user_info == user:
                    #print "no match"
                    need_append = 0
                    break
                
            if need_append == 1:
                USERS_INFO_TMP.append(user_info)
                report=report+user_info+"\n"
                #print "append"
                #print "report:%s"%report
        
        if report != '':
            print "send report:\n%s"%report
            SendMail(report)
            USERS_INFO=USERS_INFO_TMP

def SendMail(report):
    cmd = ['hostname']
    p = sub.Popen(cmd,stdout=sub.PIPE,stderr=sub.PIPE)
    out,err = p.communicate()

    if err != "":
        print err 
        sys.exit()

    Subject = "Some new vistors in %s"%out
    Body = "Here is the report:\n%s"%report 
    send.sendmail(ToAddr,Subject,Body)


while 1:
    find_users()
    time.sleep(60) 
