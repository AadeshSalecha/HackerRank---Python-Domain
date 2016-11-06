'''
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = (' '.join((' '.join(str(raw_input()).split(','))).split('.'))).split()

for i in s:
    print i
