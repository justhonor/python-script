##!/usr/bin/python
## coding:utf-8
###
## Filename: send_mail.py
## Author  : zane
## Date    : 2017-01-14
## Describe:
###
##############################################
#
import re
import sys
import smtplib  
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText  
  
# Smtpserver confg
SmtpServer = "smtp.gmail.com"
SmtpPort   = "465"

# Your own address and passwd
FromAddr = "zane.zhang@zoom.us"  
username = "zane.zhang@zoom.us"  
password = "xxxxxxxxxxxx" 

# default 
Subject  = "Please input Subject"
ToAddr   = "541469923@qq.com"
Body = "Python test mail"  

def print_help():
    print  '''
    Usage:
        python send_mail.py ToAdrr Subject Body
    e.g:
        python send_mail.py 541469923@qq.com "Python mail" "This is a test"
    '''
    sys.exit()

def check_input():
    global Subject
    global Body
    global ToAddr
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if len(sys.argv)-1 == 3:
        if email_regex.match(sys.argv[1]):
            ToAddr = sys.argv[1]
            Subject = sys.argv[2]
            Body = sys.argv[3]
        else:
            print "Number one agruments is a email address"
            print_help()
    else:
        print_help()


def sendmail(toaddr,subject,body):

    #password = raw_input("Please input passwd for %s:\n"%username)

    msg = MIMEMultipart()  
    msg['From'] = FromAddr  

    msg['To'] = toaddr  
    msg['Subject'] = subject  
    msg.attach(MIMEText(body, 'plain'))  
  
    try :
        server = smtplib.SMTP_SSL(SmtpServer,SmtpPort)  
        server.login(username,password)  
    except Exception,e:
        print "login error:",e
        server.quit()
        sys.exit()

    text = msg.as_string()
    
    try :
        server.sendmail(FromAddr, toaddr, text)
    except Exception,e:
        print "send error:",e
        server.quit()
        sys.exit()

    print "Send successed!!!"
    server.quit()
    



if __name__=="__main__":
    check_input()
    sendmail(ToAddr,Subject,Body)
