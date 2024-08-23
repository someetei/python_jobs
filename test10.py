#!/usr/bin/python
# -*- coding: cp1252 -*-
"""
Author: Vinícius Rodrigues da Cunha Perallis
http://www.dbatodba.com
Function:Check if instance is running fine 

Created in: 01/14/2009
Updated in: 01/15/2009   

########################################################################################
Descripton: This program return 2 types of value:
0 = normal
2 = error

If all instances running properly,then the exit of program is 0.
If any instance is down, then the exit of program is 2.
########################################################################################
"""
import string
import os
import time
import sys

try:
  number_of_instances=int(sys.argv[1])
except:
  #default value of number of instances
  number_of_instances=1

resultado=0
db2sysc=str.split(os.popen("ps -ef | awk 'BEGIN {QTDE=0} {if ($8 ~ /db2sysc/) {QTDE=QTDE+1}}END {print QTDE}'").read())
db2sysc_real=int(db2sysc[0])

if db2sysc_real==number_of_instances:
     if number_of_instances==1:  
         print ("OK: "+str(number_of_instances)+" Instance is running properly.")
     elif number_of_instances>1:
         print ("OK:,"+str(number_of_instances)+",instances are running properly.")
     sys.exit(0)
else:
     if number_of_instances==1:  
         print ("CRITICAL: "+str(number_of_instances)+"-"+str(db2sysc_real)+",instances is DOWN")    
     elif number_of_instances>1:
         print ("CRITICAL: "+str(number_of_instances)+"-"+str(db2sysc_real)+",instances are DOWN" )    
     sys.exit(2)