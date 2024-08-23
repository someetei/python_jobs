#!/usr/bin/python
# -*- coding: cp1252 -*-

#Import the libraries to use the OS commands and date and time functions
import os
import time
#import string

####### Variable to be configurated by user #######

#Directory where will store the db2diag and nfy zipped
dir_target='/tmp/python_jobs/outdir/'

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
### move to TSM ###
#move_db2diag='dsmc ar "' + file_diag + '_*" -delete files '

#nfy
db2diag_nfy='db2diag -A ' + file_nfy
gzip_nfy='gzip ' + file_nfy + '_*'
move_nfy='mv ' + file_nfy + '_* '+dir_target
#move_nfy='dsmc a "' + file_nfy + '_*" -delete files '

#Open the files to written
f=open(file_output,'a')

#Function to execute the rename, compress and move commands
def compress(log,gzip,move,file):
     if (os.system(log) == 0):
          file.write("1 - Command db2diag -A completed successufully\n")
          if (os.system(gzip) == 0):
               file.write("2 - Command gzip completed successfully\n")
               os.system(move)
               file.write("3 - Script compress_db2diag completed successfully !!!\n")
          else:
               file.write("2 - Command gzip failed\n")
     else:
          file.write("1 - File to be compressed doesn't exist\n")


######### Move all .gz to dir_target ###########
os.system('mv ' + diagpath[0] + 'DIAG0000/*.gz ' + dir_target)

########## Compress nfy #########

f.write("\n------------  Compressing db2inst1.nfy ... - Date: " + time.strftime('%Y%m%d%H') + " ------------- \n\n")
compress(db2diag_nfy,gzip_nfy,move_nfy,f)

########## Compress diag #########
f.write("\n------------ Compressing db2diag.log ... - Date: " + time.strftime('%Y%m%d%H') + " ------------- \n\n")
compress(db2diag_db2diag,gzip_db2diag,move_db2diag,f)

f.close()
