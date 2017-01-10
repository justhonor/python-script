#!/usr/bin/python
# coding:utf-8
##
# Filename: cp_info_into_file.py
# Author  : zane
# Date    : 2017-01-09
# Describe:
##
#############################################
import os 
#from ipdb import set_trace

SOURCE='/home/aiapple/git/python-script'
wildcard=".readme"
DESTFILE='/home/aiapple/git/python-script/README.md'
#find xxx.readme
def Find_spec_file(dirt,wildcard):
	exts=wildcard.split(" ")
	output=[]
	for root,subdirs,files in os.walk(dirt):
	    for name in files:
		for ext in exts:
		    if name.endswith('.readme'):
			#print "%s/%s"%(root,name)
			output.append("%s/%s"%(root,name))
			#print output
	return output

#Find_spec_file(SOURCE,wildcard)
def process_info(destfile):
    md=open('%s'%destfile,'a')
    # Find xxx.readme with fullpath
    for files in Find_spec_file(SOURCE,wildcard):
	 f=open('%s'%files,'r')
	 for line in f.readlines():
		 # Add <br> for each line
	#	 if not line.isspace():
	#		 line=line+" <br>"
		
		 # Is first line add a '#'
		 if line[0]=='#':
			 line=line[:0]+"#"+line[0:]

		 # Is heading add four '#' 
		 if line[0].isupper():
			 line=line[:0]+"###"+line[0:]
		

		 # Write to README.md
#		 set_trace()
		 md.write('%s\n'%line)

	 f.close()
    md.close()

# Rebuild README.md
if __name__=="__main__":
    f=open('%s'%DESTFILE,'wr')
    f.write("# python-script\n")
    f.write("There are some  python scripts that similar to shell scripts which in my-bash-shell \n")
    f.write("\n\n")
    f.close()
    process_info(DESTFILE)
