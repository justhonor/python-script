#!/usr/bin/python
# coding:utf-8
##
# Filename: login_manage.py
# Author  : zane
# Date    : 2017-01-12
# Describe:
##
#############################################

import os
import sys
import subprocess as sub
#import ipdb

pubrsa="/home/zane/.ssh/id_rsa.pub"
def Print_help():
    print"  Usage:"
    print"        Login : "
    print"                python login_manage.py [-i] alias_name"
    print"        Manage:                                       "
    print"                python option [parameter1|parameter2...]  "
    print               
    print"                Add                            "              
    print"                        -a|add alias_name user host"              
    print"                Delete                             "              
    print"                        -d|del alias_name          "              
    print"                Change                             "              
    print"                        -c|chg src_name dest_name  "              
    print"                Look                               "              
    print"                        -l|look                     "              
    print"                Help                               "              
    print"                        -h|help                    "              
    sys.exit()


def Inital_key():
    initcmd = "ssh-keygen -t rsa "
    os.system(initcmd)        

def Look():
    try:
        os.system("cat login.cnf")
    except:
        print "cat login.cnf error"
    sys.exit()

def Login(alias):
    # judege whether the alias exsits
    alsext=0
    if not os.path.exists('login.cnf'):
        print "Alias not exsits! Please add first"
        sys.exit()
    else:
        f = open('login.cnf','r')
        for line in f.readlines():
            spl=line.split()
            als=spl[0]
            # if find break
            if als == alias:
                user = spl[1]
                host = spl[2]
                alsext = 1
                f.close()
                break
    # whether need to login
    if alsext:
        logincmd="ssh %s@%s"%(user,host)
        try:
            os.system(logincmd)
        except:
            print "login failed! please check network and user correct!"
            sys.exit()
    else:
        print "Alias not exsits! Please add first"
        sys.exit()


def Delete(alias):
    if not os.path.exists('login.cnf'):
        print "login.cnf not exsits,nothing to delete! "
        sys.exit()
    else:
        f = open('login.cnf','r')
        lines = f.readlines()
        f.close()

        f = open('login.cnf','w')
        for line in lines:
            line_spt=line.split()
            if line_spt[0] != alias:
                f.write(line)
        f.close()


def Add(alias,user,host):

    # judege whether the alias exsits
    if not os.path.exists('login.cnf'):
        try:
            p = sub.Popen(['ssh-copy-id','-i','%s'%pubrsa,'%s@%s'%(user,host)],stdout=sub.PIPE,stderr=sub.PIPE)
            output,errors = p.communicate()
            #print "errors:"%errors 
        except:
            print "copy rsa.pub to dest error!"
            sys.exit()

        f = open('login.cnf','a+')
        f.write('%s %s %s\n'%(alias,user,host))
        f.close()
    else:
        # if alias exsits sys.exit()
        f = open('login.cnf','a+')
        for line in f.readlines():
            spl=line.split()
            als=spl[0]
            #ipdb.set_trace()
            if als == alias:
                print "alias exsits please retry!"
                f.close()
                sys.exit(1)
        try:
            p = sub.Popen(['ssh-copy-id','-i','%s'%pubrsa,'%s@%s'%(user,host)],stdout=sub.PIPE,stderr=sub.PIPE)
            output,errors = p.communicate()
            #print "output:"%output
            #print "errors:"%errors 
        except:
            print "copy rsa.pub to dest error!!"
            f.close()
            sys.exit()

        f.write('%s %s %s\n'%(alias,user,host))
        f.close()
    

def Change(src_alias,dest_alias):
    if not os.path.exists('login.cnf'):
        print "login.cnf not exsits,nothing to change! "
        sys.exit()
    else:
        f = open('login.cnf','r')
        lines = f.readlines()
        f.close()

        f = open('login.cnf','w')
        for line in lines:
            line_slt=line.split()
            if line_slt[0] != src_alias:
                f.write(line)
            else:
                line_slt[0]=dest_alias
                newline=line_slt[0]+" "+line_slt[1]+" "+line_slt[2]+" "+"\n"
                f.write(newline)
        f.close()

def Input_check():
    # Numbers of parameters can also be 1,2,3
    if len(sys.argv)-1 == 1:
        if sys.argv[1] == '-h' or sys.argv[1] == 'help':
            Print_help()
        elif sys.argv[1] == '-l' or sys.argv[1] == 'look':
            Look()
        else:
            Login(sys.argv[1])

    elif len(sys.argv)-1 == 2:
        if sys.argv[1] == '-i':
            Login(sys.argv[2])
        elif sys.argv[1] == '-d':
            Delete(sys.argv[2])
        else:
            Print_help()

    elif len(sys.argv)-1 == 3:
        if sys.argv[1] == '-c':
            Change(sys.argv[2],sys.argv[3])
        else:
            Print_help()

    elif len(sys.argv)-1 == 4:
        if sys.argv[1] == '-a':
            Add(sys.argv[2],sys.argv[3],sys.argv[4])
        else:
            Print_help()

    else:
        Print_help()

Input_check()
