#!/usr/bin/python
# -*- coding: utf-8 -*-
# Install : ibm_db package
# Command : pip install ibm_db

from ibm_db import connect
import ibm_db_dbi
import csv

DBdetails = \
    connect('DATABASE=sample;HOSTNAME=172.18.0.2;PORT=50000;PROTOCOL=tcpip;UID=db2inst1;PWD=db2inst1;'
            , '', '')
conn = ibm_db_dbi.Connection(DBdetails)

# Execute the SQL script

with open('test3.sql', 'r') as script_file:
    sql_script = script_file.read()
    cursor = conn.cursor()
    cursor.execute(sql_script)

# Fetch and export the result set in batches of 5,000 rows

fetch_size = 5000
with open('/tmp/python_jobs/outdir/test3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])
    while True:
        rows = cursor.fetchmany(fetch_size)
        if not rows:
            break
        writer.writerows(rows)

# Close the database connection

cursor.close()
conn.close()
