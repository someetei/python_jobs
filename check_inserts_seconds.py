#!/usr/bin/python
# -*- coding: 1252 -*-

"""
Author: 
Script Name:check_inserts_seconds.py
Function: Check rowsinserted per seconds in DB2 Databases
Created in: 01/23/2009
"""

import sys
import time
import ibm_db
import ibm_db_dbi as db

#Get the database name and the number of execution from command line
try:
   database=sys.argv[1]
except:
   print("Please enter the database name")
   sys.exit(1)
try:
   num_executions=int(sys.argv[2])
except:
   print("Please enter the number of execution")
   sys.exit(1)

#Create a database connection

# ESTABLISH THE CONNECTION

try:
    conn = db.connect("DATABASE=dochadr;HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=tcpip;UID=db2inst1;PWD=db2inst1;", "", "")
	return conn
	curs = conn.cursor()
except:
    print("failed to connect to database.")

for i in range(num_executions):
     curs.execute('select ROWS_INSERTED from sysibmadm.snapdb')
     rows1 = curs.fetchone()
     time.sleep(2)
     curs.execute('select ROWS_INSERTED from sysibmadm.snapdb')
     rows2 = curs.fetchone()
     print(rows2[0] - rows1[0])/2

#Close the database connection
curs.close()
conn.close() 




