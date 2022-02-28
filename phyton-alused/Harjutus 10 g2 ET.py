#############
#Erik Teppan#
#IT-21      #
#28.02.2022 #
#############
import re
fh = open('Paroolid.txt')
for line in fh:
    if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", line):
        print(line,end='') 
fj = open('Paroolid.txt')        
for line in fj:
    if re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", line):
        print(line,end='')