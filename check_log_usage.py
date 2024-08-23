#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Author: somchand heisnam
Script Name: check_log_usage.py
Function:Check the log usage in DB2 DATABASE.
Date: 



########################################################################################

Descripton: This program return 4 types of value:

0 = normal
1 = warning
2 = error
3 = unknown error



If the percentage of log usage is < threshold_warning, then the exit of program is 0.
If the percentage of log usage is >= threshold_warning, then the exit of program is 1.
If the percentage of log usage is threshold_error, then the exit of program is 2.
If is not possible connect to database, then the exit of program is 3.

########################################################################################

"""

import string
import os
import time
import sys

database = sys.argv[1]
try:
    threshold_warning = sys.argv[2]
except:
    threshold_warning = str(80)
try:
    threshold_severe = sys.argv[3]
except:
    threshold_severe = str(90)

if os.system('db2 connect to ' + database + ' > /dev/null') == 0:
    logs = string.split(os.popen('db2 connect to ' + database
                        + "; db2 'select int((float(total_log_used)/float(total_log_used+total_log_available))*100) from sysibmadm.snapdb'"
                        ).read())
    if logs[20] < threshold_warning:
        print ('OK: Utilization of logs is: ' + logs[20] \
            + '% | log-db2 ' + database + ':' + logs[20] + '%;' \
            + threshold_warning + ';' + threshold_severe)
        sys.exit(0)
    elif logs[20] >= threshold_warning and logs[20] < threshold_severe:
        print ('WARNING: Utilization of logs more than ' \
            + threshold_warning + '% | log-db2 ' + database + ':' \
            + logs[20] + '%;' + threshold_warning + ';' \
            + threshold_severe)
        sys.exit(1)
    elif logs[20] >= threshold_severe < 101:
        print ('CRITICAL:  Utilization of logs more than ' \
            + threshold_severe + '% | log-db2 ' + database + ':' \
            + logs[20] + '%;' + threshold_warning + ';' \
            + threshold_severe)
        sys.exit(2)
    else:
        print ('UNKNOWN: It is no possible execute select command on ' \
            + database)
        sys.exit(3)
else:
    print ('UNKNOWN: It is no possible to connect on ' + database)
    sys.exit(3)

