#!/usr/bin/python
# -*- coding: cp1252 -*-

#Import the libraries to use the OS commands and date and time functions
import os
import time
#import string

####### Variable to be configurated by user #######

#Directory where will store the db2diag and nfy zipped
dir_target='/tmp/python_jobs/outdir'

####### db2diag path ########

diagpath=str.split(os.popen("db2 get dbm cfg| grep -i DIAGPATH| awk '{print $7}'").read())
file_nfy=diagpath[0] + 'DIAG0000/db2inst1.nfy'
file_diag=diagpath[0] + 'DIAG0000/db2diag.log'

#File where will received the error messages from this scriot
file_output=dir_target + '/compress_db2diag.log'

####### Assembly of commands to be executed ########
#db2diag
db2diag_db2diag='db2diag -A ' + file_diag
gzip_db2diag='gzip ' + file_diag + '_*'
#### Choose the method to move your logs: move to another directory or move to TSM ####

### move to directory ###
move_db2diag='mv ' + file_diag + '_* '+dir_target
print (move_db2diag)
### move to TSM ###
#move_db2diag='dsmc ar "' + file_diag + '_*" -delete files '

#nfy
db2diag_nfy='db2diag -A ' + file_nfy
gzip_nfy='gzip ' + file_nfy + '_*'
move_nfy='mv ' + file_nfy + '_* '+dir_target
print (move_nfy)
#move_nfy='dsmc a "' + file_nfy + '_*" -delete files '

