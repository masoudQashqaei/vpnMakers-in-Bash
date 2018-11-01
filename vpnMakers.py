#a script for an easier connection to vpnmakers in Bash terminal
#author: masoud qashqai
#must run as sudo 

import subprocess
from subprocess import Popen ,STDOUT ,PIPE
import time

#use uk server
connection = Popen(["sudo", "openconnect", "uk.cisadd2.com"] , stdin=PIPE, stdout=PIPE , universal_newlines=True )

time.sleep(1)

yes = 'yes'
#set username and password
username='username'
passwd='passwd'

concat_query = "{}\n{}\n{}".format(yes, username,passwd)
connection.communicate(concat_query,timeout=10000)