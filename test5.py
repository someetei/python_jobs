#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#import getpass
import ibm_db
#import pdb
#pdb.set_trace()
# main program

try:
    database=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
except:
    print ("Please provide the database name")
    sys.exit(3)

if passwd == None or passwd == '':
    print ('The password you entered is incorrect.')
    exit(-1)

conn_string = "DATABASE="+database+";HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID="+user+";PWD="+passwd+";"
connID = ibm_db.connect(conn_string, "", "")

# If the connection fails for any reason an uncaught exception is thrown
# and the program will exit with an error.
# Add new designer employees to the employee table

sql = """INSERT INTO emp_test (empno, firstnme, midinit, lastname,workdept, phoneno, hiredate, job, edlevel, sex, birthdate,salary, bonus, comm) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
stmt = ibm_db.prepare(connID, sql)

if stmt:
    inserts = 0
with open('/tmp/python_jobs/outdir/test3.csv') as f:
    line = f.readline()

    
while len(line) > 0:
    emp_list = line.split(',')
    print (emp_list)
    
for i in range(0, len(emp_list)):
    emp_list[i] = emp_list[i].rstrip("' \n")
    emp_list[i] = emp_list[i].lstrip("' ")
emp = tuple(emp_list)
result = ibm_db.execute(stmt, emp)

if result is False:
    print ('Unable to execute the SQL statement.')
exit(-1)

inserts += 1
line = f.readline()
print (str(inserts) + ' employees inserted successfully.')

# Now delete those new tests

ibm_db.exec_immediate(connID,"delete from emp_test where empno = '000350'")
ibm_db.exec_immediate(connID,"delete from emp_test where empno = '000360'")
ibm_db.exec_immediate(connID,"delete from emp_test where empno = '000370'")
ibm_db.exec_immediate(connID,"delete from emp_test where empno = '000380'")
print ('4 employees deleted successfully.')
ibm_db.close(connID)
exit(0)
