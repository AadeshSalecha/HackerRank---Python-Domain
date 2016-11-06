'''
Title     : Validating phone numbers
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
for i in range(input()):
    num = str(raw_input())
    tmp = (re.search(r'[789](\d){1,14}',num))
    if tmp:
        if tmp.group() == num and len(num) == 10:
            print "YES" 
        else:
            print "NO"
    else:
        print "NO"
