#!/usr/bin/python
# coding:utf-8
##
# Filename: connect_mysql.py
# Author  : aiapple
# Date    : 2017-01-08
# Describe:
##
#############################################
import os
import mysql.connector as connector

# create a connection object
con = connector.connect(host="127.0.0.1",port=3306,user="zane",passwd="000000",db="zane")

# create a cursor
cursor = con.cursor()

# drop 
drop_sql = "drop table if exists names"
try:
	cursor.execute(drop_sql)
except Exception,e:
	print "drop error: ",e
# create 
create_sql = (
"create table names ("
"  id TINYINT NOT NULL AUTO_INCREMENT, "
"  name VARCHAR(30) DEFAULT '' NOT NULL,"
"  info TEXT DEFAULT '' ,"
"  age TINYINT DEFAULT '30', "
"  PRIMARY KEY (id))"
)
try:
	cursor.execute(create_sql)
except Exception,e:
	print "create error: ",e

info = "abc" * 10
# insert 3 records
names = (('Geert', info, 30), ('Jan', info, 31), ('Michel', info, 32))
insert_sql = "INSERT INTO names (name, info, age) VALUES (%s, %s, %s)"
try:
	cursor.executemany(insert_sql,names)
except Exception,e:
	print "insert many error: ",e

# insert 1 record
insert_sql1="insert into names(name,info,age) values('zane','haha',27)"
try:
	cursor.execute(insert_sql1)
except Exception,e:
	print "insert one error: ",e
	
# update 
update_sql = "update names set age=100 where name='zane'"
try:
	cursor.execute(update_sql)
except Exception,e:
	print "update error: ",e

# delete 
delete_sql = "delete from names where age=32"
try:
	cursor.execute(delete_sql)
except connector.Error,e:
	print "delete error: ",e

# commit all transactions
con.commit()

# select 
# read a record from cursor
select_sql = "select * from names"
try:
	cursor.execute(select_sql)
except Exception,e:
	print "select error: ",e

#print records and columns
alldata  = cursor.fetchall()
for data in alldata:
	print data
	print "%s %s "%(data[1],data[2]) 

# close cursor and connection object
cursor.close()
con.close()

