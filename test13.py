#!/usr/bin/python
# -*- coding: cp1252 -*-

"""
Author: Vinícius Rodrigues da Cunha Perallis
Function:Check the ipercentage of locks waitl 
Script Name: locks_wait.py
Date: 01/23/2009

########################################################################################

Descripton: This program return 3 types of value:
0 = normal
1 = warning
2 = error
3 = unknown error

If the percentage of locks waiting per applications is < threshold_warning, then the exit of program is 0.
If the percentage of locks waiting per applications is >= threshold_warning, then the exit of program is 1.
If the percentage of locks waiting per applications is >= is threshold_error, then the exit of program is 2.
If is not possible connect to database, then the exit of program is 3.
#######################################################################################

"""
import string
import os
import time
import sys
import ibm_db

#Get the variables from command line

try:
    database=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
    appl_minimal=sys.argv[4]
    threshold_warning=sys.argv[5]
    threshold_severe=sys.argv
except:
    print ("Please provide the database name, user, password,minimal applications, threshold warning, threshold critical")
    sys.exit(3)

# Connect to database
conn_string = "DATABASE="+database+";HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID="+user+";PWD="+passwd+";"
conn = ibm_db.connect(conn_string,"","")
if conn:
    print("Connection ...... [SUCCESS]")
else:
    print("Connection ...... [FAILURE]")
    sys.exit(3)

# Select the number of applications and the number of applications in lock-wait 
sql = "select locks_waiting, (int(appls_cur_cons) -1) from sysibmadm.snapdb"
exe = ibm_db.exec_immediate(conn,sql)
rows = ibm_db.fetch_tuple(exe)
appl=int(rows[1])
locks=int(rows[0])
if locks==0:
   print ("NORMAL: NO LOCKS WAITING")
   sys.exit(0) 
else:
   percentage=(float(locks)/float(appl))*100

if int(appl)>=int(appl_minimal) :
   if percentage>=float(threshold_warning) and percentage<float(threshold_severe):
      print ("WARNING: The percentage of locks waiting per applications is",percentage)
      sys.exit(1)
   elif percentage>float(threshold_severe):
      print ("CRITICAL The percentage of locks waiting per applications is",percentage) 
      sys.exit(2)
   else:
      print ("NORMAL: The percentage of locks waitning per application is",percentage)
      sys.exit(0)
else:
    print ("The minimal number of applications connected was not reach to validade this script")
    sys.exit(0)