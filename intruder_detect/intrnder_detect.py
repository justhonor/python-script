#!/usr/bin/python
# coding:utf-8
##
# Filename: intrnder_detect.py
# Author  : aiapple
# Date    : 2017-01-10
# Describe:
##
#############################################
import re
import pdb

AUTHLOG='auth.log'
TOPN=2
# process auth.log return normal format
def process_log():
	log=[]
	try:
		f=open('tt','r')
	except Exception,e:
		print "open eorr",e

	for line in f.readlines():
			if re.findall('invalid',line)==[] and re.findall('Failed password',line)==['Failed password']:
					lineshort=line.split()
					log.append("%s %s %s %s %s "%(lineshort[0],lineshort[1],lineshort[2],lineshort[8],lineshort[10]))
					#print log
	f.close()
	return log

# Count each ip attempt times
def count_ip_times():
	# dic{'ip':times}
	dic={}
	for line in process_log():
		needinit=1
		fieds=line.split()	
		ip=fieds[-1]
		#print ip
		
		if dic.keys() == []:
				dic['%s'%ip]=0
				needinit=0
		else:
			for k in dic.keys():
				if k == ip:
					needinit=0

		# ip have initialization
		# find the key and plus the value
		if needinit == 1:
				dic['%s'%ip]=1
		else:
		 		for key in dic:
					if key == ip:
						dic['%s'%ip]=dic['%s'%ip]+1
	return dic

def find_topn_ips():
		top_ip_times=[([0]*2)for i in range(TOPN)]
		dic = count_ip_times()
		print dic
		for key in dic:
				print "%s:%s"%(key,dic['%s'%key])
				for i in range(TOPN):
						pdb.set_trace()
						if i == TOPN-1 and dic['%s'%key] > int(top_ip_times[i][1]):
								top_ip_times[i][1]=dic['%s'%key]
								top_ip_times[i][0]=key
								break
						if dic['%s'%key] > int(top_ip_times[i][1]) and dic['%s'%key] <= int(top_ip_times[i+1][1]):
								top_ip_times[i][1]=dic['%s'%key]
								top_ip_times[i][0]=key
								break
		print top_ip_times
#process_log()
#count_ip_times()
find_topn_ips()

