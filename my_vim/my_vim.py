#!/usr/bin/python
# coding:utf-8
##
# Filename  : my_vim.py
# Autho     : aiapple
# Date      : 2016-12-28
# Describe  :
##
############################################

import sys
import os

is_sh = 0
is_py = 0
is_rd = 0


def print_help():
    print "    e.g  :python %s test.py" % sys.argv[0]
    print "    file :xxx.sh xxx.py xxx.readme"


#############################################
# print "this is : %s" %sys.argv[0]
if len(sys.argv) != 2:
    print " please input one file!\n"
    print_help()
    exit()
else:
    if os.path.exists('%s' % sys.argv[1]):
        print "   %s have exists" % sys.argv[1]
        str = raw_input("   quit:q  remove and rebuild:c\n")
        if str != 'c':
            exit()


def Is_rd():
    # print "this is is_rd()"
    file = open('%s' % sys.argv[1], 'wr')
    file.write("#This is %s\n\n" % sys.argv[1])
    file.write("Introduction\n\n")
    file.write("Example\n\n")
    file.write("Test\n\n")
    file.close()
    os.system('vim %s' % sys.argv[1])


def Is_sh():
    # print "this is is_sh()"
    filename = sys.argv[1]
    # print "filename:%s\n"%filename

    author = os.popen('whoami').read()
    # print "author:%s\n"%author

    date = os.popen('date +%F').read()
    # print "date:%s\n"%date

    file = open('%s' % sys.argv[1], 'wr')
    if is_sh:
        file.write("#!/bin/bash\n")
    elif is_py:
        file.write("#!/usr/bin/python\n")
        file.write("# coding:utf-8\n")
    # file.write("#############################################\n")
    file.write("##\n")
    file.write("# Filename: %s\n" % filename)
    file.write("# Author  : %s" % author)
    file.write("# Date    : %s" % date)
    file.write("# Describe:\n")
    file.write("##\n")
    file.write("#############################################\n")
    file.close()
    os.system('vim %s' % sys.argv[1])


extend = os.path.splitext(sys.argv[1])
if extend[1] == '.readme':
    is_rd = 1
    Is_rd()
elif extend[1] == '.sh':
    is_sh = 1
    Is_sh()
elif extend[1] == '.py':
    is_py = 1
    Is_sh()
else:
    print "Please enter correctly!!!\n"
    print_help()
    exit()
