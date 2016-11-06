'''
Title     : Validating Postal Codes
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = str(raw_input())
tmp = re.match(r'([1-9][0-9]{5})(.*$)', s)
try:
    tmp1 = re.findall(r'(?=(\d)\d\1)', tmp.group(1))
    print (len(tmp1) < 2 and tmp) and (s == tmp.group(1))
except:    
    print False




