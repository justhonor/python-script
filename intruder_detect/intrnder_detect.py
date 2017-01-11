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
import ipdb
#import subprocess
import socket

AUTHLOG='auth.log'
TOPN=3
DEBG=0
LOG=[]
# process auth.log return normal format
def process_log():
        global LOG
	LOG=[]
	try:
		f=open(AUTHLOG,'r')
	except Exception,e:
		print "open eorr",e

	for line in f.readlines():
			if re.findall('invalid',line)==[] and re.findall('Failed password',line)==['Failed password']:
					lineshort=line.split()
					LOG.append("%s %s %s %s %s "%(lineshort[0],lineshort[1],lineshort[2],lineshort[8],lineshort[10]))
					#print LOG 
	f.close()
	if DEBG: ipdb.set_trace()
        return LOG
	

# Count each ip attempt times
def count_ip_times():
	# dic{'ip':times}
	dic={}
	if DEBG: ipdb.set_trace()
	for line in LOG:
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
		#print dic
		for key in dic:
				#print "%s:%s"%(key,dic['%s'%key])
				for i in range(TOPN):
			       	#	        if DEBG: ipdb.set_trace()
                                                # If key large than last one (max one)
                                                # Array move forward and update the key in last.
						if i == TOPN-1 and dic['%s'%key] > int(top_ip_times[i][1]):
                                                                for m in range(TOPN-1):
                                                                    top_ip_times[m][0]=top_ip_times[m+1][0]
                                                                    top_ip_times[m][1]=top_ip_times[m+1][1]
								top_ip_times[i][1]=dic['%s'%key]
								top_ip_times[i][0]=key
								break
                                                # if key large A and less than A+1 update A=key
						if dic['%s'%key] > int(top_ip_times[i][1]) and dic['%s'%key] <= int(top_ip_times[i+1][1]):
								top_ip_times[i][1]=dic['%s'%key]
								top_ip_times[i][0]=key
								break
                                                
		return top_ip_times

process_log()
#count_ip_times()
#find_topn_ips()

# find topIP corespond users,hostname,time period 
def find_other_info():
    top_ip_times=find_topn_ips()
    rank=1
    print "%-5s|%-10s|%-10s|%-16s|%-40s|%s"%("Sr#","USERS","TIMES","IP address","Time  range","Host name")
    for i in range(TOPN)[::-1]:
        users_statime={}
        users_endtime={}
        users_times={}
	#ipdb.set_trace()
        try:
            host=socket.gethostbyaddr("%s"%top_ip_times[i][0])
            #host=socket.gethostbyaddr("8.8.8.8")
            hostname=host[0]
        except:
            hostname="Unkown"
        #print hostname

	#ipdb.set_trace()
        for line in LOG:
            needinit=1
            if re.findall('%s'%top_ip_times[i][0],line)==['%s'%top_ip_times[i][0]]:
                 #print line 
                 fid=line.split()

                 #if fid[3]=='root':
	         #    ipdb.set_trace()
                 #    print "%s:"%top_ip_times[i][0],users_statime
                 #    print "%s:"%top_ip_times[i][0],users_endtime
                 #    print "%s:"%top_ip_times[i][0],users_times
                
                 # judge if need to initial
                 for key in users_statime:
                     if key==fid[3]:
                         needinit=0


                 if needinit:
                     users_statime['%s'%fid[3]]="%s %s %s"%(fid[0],fid[1],fid[2])
                     users_times['%s'%fid[3]]=1
                 else:
                     users_endtime['%s'%fid[3]]="%s %s %s"%(fid[0],fid[1],fid[2])
                     users_times['%s'%fid[3]]=users_times['%s'%fid[3]] + 1
	#ipdb.set_trace()
        #print "%s:"%top_ip_times[i][0],users_statime
        #print "%s:"%top_ip_times[i][0],users_endtime
        #print "%s:"%top_ip_times[i][0],users_times
        for user in users_statime:
            Time_range="%s --> %s"%(users_statime[user],users_endtime[user])
#	    ipdb.set_trace()
            print "%-5s|%-10s|%-10s|%-16s|%-40s|%s"%(rank,user,users_times[user],top_ip_times[i][0],Time_range,hostname)
        rank=rank+1
	#ipdb.set_trace()

        #print "%s:"%top_ip_times[i][0],users_statime
        #print "%s:"%top_ip_times[i][0],users_endtime
        #print "%s:"%top_ip_times[i][0],users_times

find_other_info()
