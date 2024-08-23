#!/usr/bin/python
# -*- coding: 1252 -*-

"""
Author: Vinícius Rodrigues da Cunha Perallis
http://www.dbatodba.com
Script Name:check_inserts_seconds.py
Function: Check rowsinserted per seconds in DB2 Databases

Created in: 01/23/2009
"""
import sys
import ibm_db 
import time


#Get the database name and the number of execution from command line
try:
   database=sys.argv[1]
except:
   print ("Please inform the database name")
   sys.exit(1)
try:
   num_executions=int(sys.argv[2])
except:
   print ("Please inform the number of execution")
   sys.exit(1)

#Create a database connection

try:
    #conn_string="Server=172.18.0.2;Port=50000;Database=sample;UID=db2inst1;PWD=db2inst1;"
    #conn = ibm_db.connect(conn_string,"","")
    dsn= "DRIVER={ibm db2 odbc driver};DATABASE=sample;HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;"
    conn=ibm_db.connect(dsn, "", "")
    curs=conn.cursor()
except:
    print ("Connection was unsuccessful")
    sys.exit(1)

for i in range(num_executions):
     curs.execute('select ROWS_INSERTED  from sysibmadm.snapdb')
     rows1 = curs.fetchone()
     time.sleep(2)
     curs.execute('select ROWS_INSERTED  from sysibmadm.snapdb')
     rows2 = curs.fetchone()
     print (rows2[0])
     #print (rows2[0] - rows1[0])/2

#Close the database connection
curs.close()
conn.close() 