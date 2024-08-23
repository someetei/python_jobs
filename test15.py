import pyodbc

conn = pyodbc.connect("DSN=db2dns;PWD=db2inst1")
print("Connected successfully..!!")
cursor=conn.cursor()
cursor.execute("select tabname from syscat.tables where type='T'")
rows=cursor.fetchall()
print(rows)




