#!/usr/bin/python
# coding:utf-8
##
# Filename: remove_duplicates.py
# Author  : aiapple
# Date    : 2017-01-15
# Describe:
##
#############################################
import os
import sys
import subprocess as sub
import pdb

DIR=''
all_files=[]
#Find fullname of all files 
def Find_all_files(dirt):
        output=[]
        for root,subdirs,files in os.walk(dirt):
            for name in files:
                if not name.isspace():
                    output.append("%s/%s"%(root,name))

        return output

def Dele_dupl_file(filenames):
	file_md5={}
	md5_file=[]
	for filename in filenames:		
		#print filename
        	try:
        	    p = os.popen("md5sum %s"%filename)
		    #md5_file.append(p.read())
		    output = p.read().split()
            	    md5 = output[0]
            	    #print md5
        	except Exception,e:
           	    print e
            	    sys.exit()
		file_md5['%s'%filename] = md5

	dupl=[]
	filemd5=file_md5
	for file in file_md5.keys():
		for key in filemd5.keys():
			if file != key and file_md5[file] == file_md5[key]:
				dupl.append(file)
				print "remove %s"%file
				os.remove(file)
				break
		filemd5.pop(file)

	#print dupl		 

def print_help():
	print'''
	Usage:
		python remve_duplicates.py [DIR]				
	'''
	sys.exit()

def check_input():
	global DIR
	if len(sys.argv)-1 == 1:
		if os.path.exists(sys.argv[1]):
			DIR = sys.argv[1]
		else:
		   print "Please input a directory"

	elif len(sys.argv)-1 == 0:
		DIR = os.path.curdir
	else:
		print_help()
	
check_input()
#print DIR
all_files=Find_all_files(DIR)		
#print "this is all:",all_files
Dele_dupl_file(all_files)




