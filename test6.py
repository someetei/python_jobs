#!/usr/bin/python
# -*- coding: utf-8 -*-

#import sys
#import getpass
import ibm_db
import pyodbc
import pylance

# main program
connID = pyodbc.connect("DSN=db2dns;PWD=db2inst1")

# If the connection fails for any reason an uncaught exception is thrown
# and the program will exit with an error.
# get the records from the database

sqlstmt = 'select * from department'
try:
    results = ibm_db.exec_immediate(connID, sqlstmt)
except Exception:
    pass

# If the sql statement could not be executed, display an error message and exit

if results is False:
    print ( '\nERROR: Unable to execute the SQL statement specified.')
    ibm_db.close(connID)
    exit(-1)
    
def getColNamesWidths(results):

# get the width of each column

    columns = list()
    col = 0
    numColumns = 0


try:
    numColumns = ibm_db.num_fields(results)
except Exception:
    pass

# If information about the number columns returned could not be obtained,
# display an error message and exit .

if numColumns is False:
    print ('\nERROR: Unable to obtain information about the result set produced.')
connID.closeConnection()
exit(-1)

while col < numColumns:
    col_name = ibm_db.field_name(results, col)
    col_width = ibm_db.field_width(results, col)

# the field name can be bigger than the display width

col_width = max(len(col_name), col_width)
columns.append((col_name, col_width))
col += 1
return columns  # return a list of tuples (name, size)


def populateColTitleLines(columns):

    # populate the two title lines for the results

    col = 0
    line = ''
    lines = []


# do the title line

while col < len(columns):
    (col_name, col_width) = columns[col]
    title = col_name + (col_width - len(col_name)) * ' '
    line += ' ' + title
    col += 1
lines.append(line)

# do the underlines

col = 0
line = ''
while col < len(columns):
    (col_name, col_width) = columns[col]
    line += ' ' + col_width * '-'
col += 1
lines.append(line)
return lines  # return the two title lines


def populateLines(results, headerLines):

    # print the data records

    lines = []


record = ibm_db.fetch_tuple(results)
while record is not False:
    line = ''
    col = 0
    numColumns = 0
try:
    numColumns = ibm_db.num_fields(results)
except Exception:
    pass

# If information about the number columns returned could not be obtained,
# display an error message and exit .

if numColumns is False:
    print ( '\nERROR: Unable to obtain information about the result set produced.')
    conn.closeConnection()
    exit(-1)
while col < numColumns:
    colstr = record[col]
    (name, col_width) = headerLines[col]
    coltype = ibm_db.field_type(results, col)
if record[col] is None:
    line += ' -' + (col_width - 1) * ' '
elif coltype in ('clob', 'dbclob', 'blob', 'xml', 'string'):

    # these are the string types

    line += ' ' + str(colstr) + (col_width - len(colstr)) * ' '
else:

# these are the numeric types, or at least close enough

    colstr = str(colstr)
    line += ' ' + (col_width - len(colstr)) * ' ' + colstr
    col += 1
    lines.append(line)
    record = ibm_db.fetch_tuple(results)
    return lines



# fetch SQL results and format lines

headerLines = getColNamesWidths(results)
titleLines = populateColTitleLines(headerLines)
dataLines = populateLines(results, headerLines)
selrecords = len(dataLines)

# print the result lines

for line in titleLines:
    print (line)
for line in dataLines:
    print (line)

# print the number of records returned

print ( '\n ' + str(selrecords) + ' record(s) selected.')
ibm_db.close(connID)
exit(0)

