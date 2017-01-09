# python-script
There are some  python scripts that similar to shell scripts which in my-bash-shell 



##This is analysis_dir.readme
 <br>


##### Introduction
 <br>


	Analysis the directory and give some reports.
 <br>
	Also find out some scripts that has more than N lines. (N default 150)
 <br>


	e.g:
 <br>
		a. How many scripts on the directory
 <br>
		b. How many lines of the whole scripts
 <br>
		c. The average length of those scripts
 <br>
		d. what is the longest script and how it has
 <br>
		e. what is the shortest script and how it has
 <br>
		f. what is the ratio of comments 
 <br>


##### Example
 <br>


	aiapple@ubuntu:~/git/python-script/analysis_dir$ python analysis_dir.py script/ 200 d
 <br>


##### Test
 <br>
	aiapple@ubuntu:~/git/python-script/analysis_dir$ python analysis_dir.py script/ 200 d
 <br>
		you have three correct parameters,line is 200,dir is d
 <br>
		cp script/check_cpu.sh to  d
 <br>


    		There are 36 scripts totaling 1165 lines
 <br>
    		The average of each script have 32.36 lines
 <br>
    		The ratio of comments is 14.85 % 
 <br>
    		The longest script is script/check_cpu.sh which have 217 lines 
 <br>
    		The shortest script is script/testuser2.sh which have 3 lines 
 <br>


##### Notes
 <br>
	

	a.Find the specific file type such as xxx.py, xxx.sh ..
 <br>
		import glob
 <br>
		#find *.pl
 <br>
		for filename in glob.glob(os.path.join(SOURCE,'*.pl')):
 <br>


##### Issue
 <br>
	a.Can not find files in subdirectory.
 <br>
## This is cp_info_into_file.readme
 <br>


##### Introduction
 <br>


	Add all the contents of the xxx.readme file from the python-scrit directory to README.md. 
 <br>
	And do some change for showing .
 <br>
		a.Add a '#' for first line
 <br>
		b.Add four '#' for each heading in the beging of the line.
 <br>
		c.Add <br> at end of each line
 <br>
##### Example
 <br>


##### Test
 <br>


##### Notes
 <br>
	f.write("%s\n"%line) need '\n' charictor
 <br>


##This is active_users.readme
 <br>


##### Introduction
 <br>


	Count user login informations by analysis /var/log/wtmp.
 <br>
	Except some status information such as still,crash,down.
 <br>
	Except some system user reboot,root...
 <br>


	Give a report like:
 <br>
 		         Rand User     StartTime       LastTime        Mins
 <br>
         		 1    aiapple  Dec 17 11:28    Dec 21 07:26    1514
 <br>
         		 2    user2    Dec 17 11:38    Dec 17 11:43    1
 <br>
	

##### Example
 <br>


##### Test
 <br>


##This is connect_mysql.readme
 <br>


##### Introduction
 <br>


	Python script connect to mysql with mysql.connector and execute some sql .
 <br>


	Install mysql.connector
 <br>
		a. wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.1.tar.gz
 <br>
		b. tar -zxvf mysql-connector-python-2.1.1.tar.gz
 <br>
		c. sudo python setup.py install
 <br>
##### Example
 <br>
	

	aiapple@ubuntu:~/git/python-script/connect_mysql$ python connect_mysql.py 
 <br>
##### Test
 <br>


	aiapple@ubuntu:~/git/python-script/connect_mysql$ python connect_mysql.py 
 <br>
	(1, u'Geert', u'abcabcabcabcabcabcabcabcabcabc', 30)
 <br>
	Geert abcabcabcabcabcabcabcabcabcabc 
 <br>
	(2, u'Jan', u'abcabcabcabcabcabcabcabcabcabc', 31)
 <br>
	Jan abcabcabcabcabcabcabcabcabcabc 
 <br>
	(4, u'zane', u'haha', 100)
 <br>
	zane haha
 <br>


##### Notes
 <br>


	Every update,insert,delete needs to be committed manually by connection object.
 <br>
	But drop table,create table need't.
 <br>
	con.commit()
 <br>
##This is my_vim.readme 
 <br>


##### Introduction
 <br>
	

	According to the script name add something to the new script and continue editing the new script.
 <br>


	If the name is xxx.readme,add four rows such like :
 <br>
		#This is xxx.readme
 <br>
		Introduction
 <br>
		Example
 <br>
		Test
 <br>
	

	If the name is xxx.sh or xxx.py add some other information for example:
 <br>
	xxx.py
 <br>
		#!/usr/bin/python
 <br>
		# coding:utf-8
 <br>
		##
 <br>
		# Filename : xxx.py
 <br>
		# Author   : zane
 <br>
		# Created  : 2016-12-28
 <br>
		# Describe : 
 <br>
		##
 <br>
		###########################
 <br>
	xxx.sh
 <br>
		#!/bin/bash
 <br>
		##
 <br>
		# Filename : xxx.sh
 <br>
		# Author   : zane
 <br>
		# Created  : 2016-12-28
 <br>
		# Describe : 
 <br>
		##
 <br>
		###########################
 <br>
	

##### Example 
 <br>


	zane@zane-V:~/git/python-script/my_vim$ python my_vim.py test.py
 <br>


##### Test
 <br>
	zane@zane-V:~/git/python-script/my_vim$ python my_vim.py test.py
 <br>


