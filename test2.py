# Install : ibm_db package
# Command : pip install ibm_db

import ibm_db
import sys

try:
    database=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
except:
    print ("Please provide the database name, user, password")
    sys.exit(3)

# ESTABLISH THE CONNECTION

try:
    conn_string = "DATABASE="+database+";HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=TCPIP;UID="+user+";PWD="+passwd+";"
    conn = ibm_db.connect(conn_string,"","")
    print("Successfully connected to database!")

except:
    print("failed to connect to database.")

#  FETCHING DATA:
sql = "select tabschema from syscat.tables limit 10"
stmt = ibm_db.exec_immediate(conn, sql)
result = ibm_db.fetch_assoc(stmt)


while result:
    print(result)
    result = ibm_db.fetch_assoc(stmt)

#  INSERTING DATA:

#Construct the query - replace ... with the insert statement
sql1 = "insert into abc values (30, 'Teck'),(40, 'Sam'),(50, 'John')"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, sql1)

ibm_db.commit(conn)
ibm_db.close(conn)
