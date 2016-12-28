#!/usr/bin/python 
#coding:utf-8

#############################################
##
#文件名: my_vim.py
#作者名: aiapple
#时间  : 2016-12-28
#简介  : 
##
#
############################################

import sys
import os

def print_help(): 
	print "    示例  :python %s test.py"%sys.argv[0]
	print "    文件名:xxx.sh xxx.py xxx.readme"
is_sh=0
is_py=0
is_rd=0
#############################################
#print "this is : %s" %sys.argv[0]
if len(sys.argv)!=2:
	print " 请输入一个文件名!\n"
	print_help()
	exit()
else:
	if os.path.exists('%s'%sys.argv[1]):
		print "   %s已经存在!!!" %sys.argv[1]
		str=raw_input("   退出:q  删除创建:c\n")
		if str!='c':
			exit()

def Is_rd():
	#print "this is is_rd()"
	file=open('%s'%sys.argv[1],'wr')
	file.write("#This is %s\n\n"%sys.argv[1])
	file.write("功能介绍\n\n")
	file.write("使用介绍\n\n")
	file.write("测试\n\n")
	file.close()
	os.system('vim %s'%sys.argv[1])

def Is_sh():
	#print "this is is_sh()"
	filename=sys.argv[1]
	#print "filename:%s\n"%filename

	author=os.popen('whoami').read()
	#print "author:%s\n"%author

	date=os.popen('date +%F').read()
	#print "date:%s\n"%date

	file=open('%s'%sys.argv[1],'wr')
	if is_sh:
		file.write("#!/bin/bash\n")
	elif is_py:
		file.write("#!/usr/bin/python\n")
		file.write("#coding:utf-8\n")
	#file.write("#############################################\n")
	file.write("##\n")
	file.write("#Filename: %s\n"%filename)
	file.write("#Author  : %s"%author)
	file.write("#Date    : %s"%date)
	file.write("#Describe: \n")
	file.write("##\n")
	file.write("#############################################\n")
	file.close()
	os.system('vim %s'%sys.argv[1])

extend=os.path.splitext(sys.argv[1])
if extend[1]=='.readme':
	is_rd=1
	Is_rd()
elif extend[1]=='.sh':
	is_sh=1
	Is_sh()
elif extend[1]=='.py':
	is_py=1
	Is_sh()
else:
	print "请正确输入!!!\n"
	print_help()
	exit()

