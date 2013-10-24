#!/usr/local/bin/python
# -*- coding: utf-8 -*- # Поддержка в файле кириллицы
#Определеям модули
import os,time
import smtplib
import email.utils
import base64
from email.mime.text import MIMEText
import subprocess

#os.system ("bq41d dbipcs | grep main")
p = "R2NnaHk2NjY="
pwd = p.decode('base64')

def stop():
command = "bq41d dbipcs | grep main"
proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
(dbipcs, err) = proc.communicate()
outwithoutreturn = dbipcs.rstrip('\n')
print dbipcs 

if len(dbipcs) > 1:
  command = "bq41d stop | grep "Please enter password for dba"
  proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
  (stop, err) = proc.communicate()
  outwithoutreturn = stop.rstrip('\n')
  print stop
    if len(stop) > 1:
      command = "dby"
else:
  print "x"
  

#!/usr/local/bin/python
# -*- coding: utf-8 -*- # �^�одде�^�жка в �^�айле ки�^�илли�^��^
import os,time
#import smtplib
#import email.utils
import base64
#from email.mime.text import MIMEText
import subprocess

#os.system ("bq41d dbipcs | grep main")
#p = "R2NnaHk2NjY="
#pwd = p.decode('base64')

#def stop():
dbcheck = "bq41d dbipcs | grep main"
proch = subprocess.Popen(dbcheck,stdout=subprocess.PIPE,shell=True)
(dbipcs, err) = proch.communicate()
outwithoutreturn = dbipcs.rstrip('\n')
print dbipcs

if len(dbipcs) > 1:

        shell = os.system ("bq41d stop")
        b  = int('yes\n')
        shell.stdin.write(b)
        #dbstop = "bq41d stop"
        #procs = subprocess.Popen(dbstop.stdin.write("yes\n"))
        #procs.stdin.write("yes\n")
else:
     	print "2"
