#!/usr/bin/python
# coding:utf-8
##
# Filename: re.py
# Author  : aiapple
# Date    : 2017-01-15
# Describe:
##
#############################################
import os
import subprocess as sub

print sub.check_output("pwd")
#md5=sub.check_output("md5sum ",'re.py')
#print md5
#md5=sub.check_all("md5sum ",'/home/aiapple/git/python-script/remove_duplicates/remove_duplicates.readme')
#x=os.popen("md5sum /home/aiapple/git/python-script/remove_duplicates/remove_duplicates.readme")
x=os.popen("md5sum remove_duplicates.readme")
md5 = x.read()
#p = sub.Popen(['md5sum ','/home/aiapple/git/python-script/remove_duplicates/remove_duplicates.readme'],stdout=sub.PIPE)
#md5 = p.communicate()
print md5

