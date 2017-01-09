# python-script
There are some  python scripts that similar to shell scripts which in my-bash-shell 


##This is analysis_dir.readme



###Introduction



	Analysis the directory and give some reports.

	Also find out some scripts that has more than N lines. (N default 150)



	e.g:

		a. How many scripts on the directory

		b. How many lines of the whole scripts

		c. The average length of those scripts

		d. what is the longest script and how it has

		e. what is the shortest script and how it has

		f. what is the ratio of comments 



###Example



	aiapple@ubuntu:~/git/python-script/analysis_dir$ python analysis_dir.py script/ 200 d



###Test

	aiapple@ubuntu:~/git/python-script/analysis_dir$ python analysis_dir.py script/ 200 d

		you have three correct parameters,line is 200,dir is d

		cp script/check_cpu.sh to  d



    		There are 36 scripts totaling 1165 lines

    		The average of each script have 32.36 lines

    		The ratio of comments is 14.85 % 

    		The longest script is script/check_cpu.sh which have 217 lines 

    		The shortest script is script/testuser2.sh which have 3 lines 



###Notes

	

	a.Find the specific file type such as xxx.py, xxx.sh ..

		import glob

		#find *.pl

		for filename in glob.glob(os.path.join(SOURCE,'*.pl')):



###Issue

	a.Can not find files in subdirectory.

## This is cp_info_into_file.readme



###Introduction



	Add all the contents of the xxx.readme file from the python-scrit directory to README.md. 

	And do some change for showing .

		a.Add a '#' for first line

		b.Add four '#' for each heading in the beging of the line.

		c.Add <br> at end of each line

###Example



###Test



###Notes

	f.write("%s\n"%line) need '\n' charictory



##This is active_users.readme



###Introduction



	Count user login informations by analysis /var/log/wtmp.

	Except some status information such as still,crash,down.

	Except some system user reboot,root...



	Give a report like:

 		         Rand User     StartTime       LastTime        Mins

         		 1    aiapple  Dec 17 11:28    Dec 21 07:26    1514

         		 2    user2    Dec 17 11:38    Dec 17 11:43    1

	

###Example



###Test



##This is connect_mysql.readme



###Introduction



	Python script connect to mysql with mysql.connector and execute some sql .



	Install mysql.connector

		a. wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.1.tar.gz

		b. tar -zxvf mysql-connector-python-2.1.1.tar.gz

		c. sudo python setup.py install

###Example

	

	aiapple@ubuntu:~/git/python-script/connect_mysql$ python connect_mysql.py 

###Test



	aiapple@ubuntu:~/git/python-script/connect_mysql$ python connect_mysql.py 

	(1, u'Geert', u'abcabcabcabcabcabcabcabcabcabc', 30)

	Geert abcabcabcabcabcabcabcabcabcabc 

	(2, u'Jan', u'abcabcabcabcabcabcabcabcabcabc', 31)

	Jan abcabcabcabcabcabcabcabcabcabc 

	(4, u'zane', u'haha', 100)

	zane haha



###Notes



	Every update,insert,delete needs to be committed manually by connection object.

	But drop table,create table need't.

	con.commit()

##This is my_vim.readme 



###Introduction

	

	According to the script name add something to the new script and continue editing the new script.



	If the name is xxx.readme,add four rows such like :

		#This is xxx.readme

		Introduction

		Example

		Test

	

	If the name is xxx.sh or xxx.py add some other information for example:

	xxx.py

		#!/usr/bin/python

		# coding:utf-8

		##

		# Filename : xxx.py

		# Author   : zane

		# Created  : 2016-12-28

		# Describe : 

		##

		###########################

	xxx.sh

		#!/bin/bash

		##

		# Filename : xxx.sh

		# Author   : zane

		# Created  : 2016-12-28

		# Describe : 

		##

		###########################

	

###Example 



	zane@zane-V:~/git/python-script/my_vim$ python my_vim.py test.py



###Test

	zane@zane-V:~/git/python-script/my_vim$ python my_vim.py test.py



