#import string
#import os
#import time
import sys
import ibm_db

#creating connection

try:
    database=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
except:
    print ("Please provide the database name")
    sys.exit(3)


print("Creating connection.......")
conn_string = "DATABASE="+database+";HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID="+user+";PWD="+passwd+";"
conn = ibm_db.connect(conn_string,"","")
if conn:
    print("Connection ...... [SUCCESS]")
else:
    print("Connection ...... [FAILURE]")

q = "select current_date from sysibm.sysdummy1"

try:
    exe = ibm_db.exec_immediate(conn,q)
    row = ibm_db.fetch_tuple(exe)

    while(row):
        print(row)
        row = ibm_db.fetch_tuple(exe)
except:
    print("No rows to fetch")