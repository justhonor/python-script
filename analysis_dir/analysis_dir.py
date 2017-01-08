#!/usr/bin/python
# coding:utf-8
##
# Filename: analysis_dir.py
# Author  : aiapple
# Date    : 2017-01-07
# Describe:
##
#############################################

import os
import sys
import glob

DEBG=1

#Default
LINE=50
DIR='morelines'
SOURCE='script'


def print_help():
	print "Usage:   "
	print "      python analysis_dir.py {source_dir} [n] [dest_dir]"
	print "e.g:     "
	print "      python analysis_dir.py script 100 morelines"
	exit(1)


def check_parameters():
	global SOURCE 
	global LINE 
	global DIR
	if len(sys.argv)-1 == 1:
		if os.path.isdir(sys.argv[1]):
			SOURCE=sys.argv[1]
			if DEBG:print "have one directory parameter"
		else:
			print "your should input a directory"
			print_help()
	elif len(sys.argv)-1 == 2: 
		if os.path.isdir(sys.argv[1]): 
			if sys.argv[2].isdigit():
				LINE=int(sys.argv[2])
				if DEBG:print "you have two correct parameters,line is %s"%LINE
			else:
				print "The second parameter is not a digit"
				print_help()
		else:
			print "The first parameter is not a directory"
			print_help()
	elif len(sys.argv)-1 == 3: 
		if os.path.isdir(sys.argv[1]):
			if sys.argv[2].isdigit():
				LINE=int(sys.argv[2])
				DIR=sys.argv[3]

				if DEBG:print "you have three correct parameters,line is %s,dir is %s"%(LINE,DIR)
					
			else:
				print "The two parameter is not a digit"
		else:
			print "The first parameter is not a directory"
			print_help()
	else:
		print "Input error!"
		print_help()
	

def find_files():
        global SCRIPTS
        global LINES
        global AVERG
        global LONGEST
        global LONG
        global SHORTEST
        global SHORT
        global COMMENTS
        global RATIO

	SCRIPTS=0
	LINES=0
	AVERG=0
	LONGEST=''
	LONG=0
	SHORTEST=''
	SHORT=10000
	COMMENTS=0
	RATIO=0

	#find *.pl
	for filename in glob.glob(os.path.join(SOURCE,'*.pl')):
		SCRIPTS=SCRIPTS+1
		
		#count the comments line
		lines=0
		for line in (open(filename,'r').readlines()):
			if line[0]=='#':
				COMMENTS=COMMENTS+1
			lines=lines+1
		LINES=LINES+lines
		
		#find the extreme
		if lines > LONG:
			LONG=lines
			LONGEST=filename

		if lines < SHORT:
			SHORT=lines
			SHORTEST=filename
		
		#copy file to morelines
		if lines > LINE:
			if DEBG:print "cp %s to  %s"%(filename,DIR)
			os.system('cp -ar %s %s'%(filename,DIR))
		
	#find *.py
	for filename in glob.glob(os.path.join(SOURCE,'*.py')):
		#count the comments line

		lines=0
		for line in (open(filename,'r').readlines()):
			if line[0]=='#':
				COMMENTS=COMMENTS+1
			lines=lines+1
		LINES=LINES+lines

		#find the extreme
		if lines > LONG:
			LONG=lines
			LONGEST=filename

		if lines < SHORT:
			SHORT=lines
			SHORTEST=filename

		#copy file to morelines
		if lines > LINE:
			if DEBG:print "cp %s to  %s"%(filename,DIR)
			os.system('cp -ar %s %s'%(filename,DIR))

	#find *.sh
	for filename in glob.glob(os.path.join(SOURCE,'*.sh')):
		SCRIPTS=SCRIPTS+1

		#count the comments line
		lines=0
		for line in (open(filename,'r').readlines()):
			if line[0]=='#':
				COMMENTS=COMMENTS+1
			lines=lines+1
		LINES=LINES+lines

		#find the extreme
		if lines > LONG:
			LONG=lines
			LONGEST=filename

		if lines < SHORT:
			SHORT=lines
			SHORTEST=filename

		#copy file to morelines
		if lines > LINE:
			if DEBG:print "cp %s to  %s"%(filename,DIR)
			os.system('cp -ar %s %s'%(filename,DIR))

	AVERG=float(LINES)/float(SCRIPTS) 
	RATIO=float(COMMENTS)/float(LINES)*100


def report():
	print 
	print ("    There are %s scripts totaling %s lines"%(SCRIPTS,LINES) )
	print ("    The average of each script have %.2f lines"%(AVERG) )
	print ("    The ratio of comments is %.2f %% "%(RATIO) )
	print ("    The longest script is %s which have %s lines "%(LONGEST,LONG))
	print ("    The shortest script is %s which have %s lines "%(SHORTEST,SHORT))
	print 

if __name__=="__main__":
	check_parameters()

	#created DIR
	if not os.path.exists(DIR):
		os.mkdir(DIR)
	find_files()
	report()

