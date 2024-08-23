#!/usr/bin/python
# -*- coding: cp1252 -*-
"""
Author: Vinícius Rodrigues da Cunha Perallis
http://www.dbatodba.com
Function:Check if backups were executed or not in DB2 DATABASE 

Created in: 01/14/2009
Updated in: 01/15/2009   

########################################################################################
Descripton: This program return 3 types of value:
0 = normal
1 = warning
3 = unknown error

If the there is backup image, then the exit of program is 0.
If the there is not backup image, then the exit of program is 1.
If is not possible connect to database or if is not possible to perform any command, then the exit of program is 3.
########################################################################################
"""
import string
import os
import time
import sys

database=sys.argv[1]
threshold_warning=sys.argv[2]
resultado=0
if (os.system("/home/db2inst1/sqllib/bin/db2 connect to " + database +" > /dev/null") == 0):
    backup=str.split(os.popen("/home/db2inst1/sqllib/bin/db2 connect to " + database + ";/home/db2inst1/sqllib/bin/db2 'select 1 from sysibmadm.SNAPDB where LAST_BACKUP > current timestamp - "+  threshold_warning + " days'  | grep -i selected |awk '{print $1}' ").read())
    try:     
        if backup[18] == "1":
            print ("OK: Backup on DB "+database+" was completed successfully in the last " + threshold_warning + " days")
            resultado=0
        elif backup[18] == "0":
            print ("WARNING: NO BACKUP in the last " + threshold_warning + "days" )
            resultado=1
    except:
        print ("UNKNOWN: It is no possible execute select command on "+ database )       
        resultado=3     
else:
     print ("UNKNOWN: It is no possible to connect on "+ database)
     #resultado=3

if resultado==0:
   sys.exit(0)
elif resultado==1:
   sys.exit(1)
elif resultado==3:
   sys.exit(3)
