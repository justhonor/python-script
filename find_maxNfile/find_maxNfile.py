#!/usr/bin/python
# coding:utf-8
##
# Filename: find_maxNfile.py
# Author  : zane
# Date    : 2017-01-10
# Describe:
##
#############################################

import os
import sys
import shutil
from ipdb import set_trace

SOURCE='cc'
TOPN=2
DEBG=1

def print_help(): 
    print 
    print " Usage: " 
    print "       python %s [src] [N] "%sys.argv[0] 
    print 
    print "       src is a directory!"
    print "       N   is a digit!"
    exit

def check_input():
    global SOURCE
    global TOPN
    if len(sys.argv)-1 == 2:
        if not sys.argv[2].isdigit() or not os.path.exists(sys.argv[1]):
            print_help()
        SOURCE=sys.argv[1]
        TOPN=int(sys.argv[2])
    elif len(sys.argv)-1 == 1:
        if not os.path.exists(sys.argv[1]):
            print "Path %s not exists!"%sys.argv[1]
            exit
        SOURCE=sys.argv[1]
    elif len(sys.argv)-1 == 0:
        print
    else:
        print_help()

#Find fullname of all files 
def Find_spec_file(dirt):
	output=[]
	for root,subdirs,files in os.walk(dirt):
	    for name in files:
                if not name.isspace():
		    output.append("%s/%s"%(root,name))
    
	return output

def Get_TopNfile():
    # Create array to store topN
    # First column store fullname,second column store filesize
    # The last line store max file
    topN = [([0] * 2) for i in range(TOPN)]
    for name in Find_spec_file(SOURCE):
        #print name
        filesize = os.path.getsize(name) 
        # Determine the update location
        for i in range(TOPN):
            # If up to the last line
            # update last line with filesize
            if i == TOPN-1 and filesize > int(topN[i][1]):
#                set_trace()
                topN[i][1]=filesize
                topN[i][0]=name
                break
            # filesize more than line1 less than line2
            # update line1 with filesize
            if filesize > int(topN[i][1]) and filesize <= int(topN[i+1][1]):
#               set_trace()
                topN[i][1]=filesize
                topN[i][0]=name
                break

    return topN

def Interact():
    topN = Get_TopNfile()
    print "\n    Here are top %s largest files in %s"%(TOPN,SOURCE)
    for i in range(TOPN)[::-1]:
        sizeKb=topN[i][1]/1024
        print "                 %s: %sKB"%(topN[i][0],sizeKb)

    print "    The options:" 
    print "                 a   Delete all files above" 
    print "                 d   Delete the specify file" 
    print "                 b   Backup the file to the directory" 
    print 
    print "    Others for end the script" 
    
    inp=raw_input()
    if inp == 'a':
        if DEBG : set_trace()
        for i in range(TOPN)[::-1]:
            os.remove('%s'%topN[i][0])
    elif inp == 'd':
        filename = raw_input("Please input fullpath filename for delete!\n")
        if not os.path.isfile(filename):
            print "%s not exsit"%filename
            exit
        if DEBG : set_trace()
        os.remove(filename)
    elif inp == 'b':
        filename,bckdir = raw_input("Please input backup filename and destdir\n").split()
        if not os.path.isfile(filename):
            print "%s not exsit"%filename
            exit
        if not os.path.exists(bckdir):
            os.mkdir(bckdir)
        if DEBG : set_trace()
        shutil.copy2(filename,bckdir)
    else:
            exit

if __name__=="__main__":
    check_input()
    Interact()
