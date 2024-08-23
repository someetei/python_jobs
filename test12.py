#!/usr/bin/python
# -*- coding: cp1252 -*-
"""
Author: Vinícius Rodrigues da Cunha Perallis
Script Name: check_dbs_conn.py
Function:Check databases connectivity 
Date: 28/01/2009

########################################################################################
Descripton: This program return 2 types of value:
0 = NORMAL
2 = CRITICAL

If all databases are connectable,then the exit of program is 0.
If at least one database is not connectable, then the exit of program is 2.
########################################################################################
"""
#import string
import os
#import time
import sys

#Variables
count=0
count2=0
dbs=[]
errors=[]
d_errors=''
flag=0

#Get all command line parameters and check if is possibe to connect to all databases
for database in sys.argv:
   #"If clause" to ignore the fist parameters (script name)
   if count==1:  
       if os.system("/home/db2inst1/sqllib/bin/db2 connect to " +database+" > /dev/null")==0:
            pass
       #get the dabatase name that was not possible to connect, and the error name
       else:
         errors_total=str.split(os.popen("/home/db2inst1/sqllib/bin/db2 connect to " + database).read()) 
         errors.append(errors_total[0])
         dbs.append(database)
         flag=1 
   count=1

#Build the phrase with database names and its errors
for i in dbs:
  d_errors=d_errors + " " + i + ":"+errors[count2] + " | "
  count2+=1

#Show the message
if flag==1:
   print ("CRITICAL: It was not possible to connect to DB:" + d_errors)
   sys.exit(2)
else:
   print ("OK : Banco(s) connectable")
   sys.exit(0)


 


