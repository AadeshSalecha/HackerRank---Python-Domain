'''
Title     : Validating and Parsing Email Addresses
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import email.utils
import re
def valid(name, email):
    tmp = re.match(r'([a-zA-Z][a-zA-Z-._0-9]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})(.*$)', email[1:-1])
    if tmp:
        tmp = tmp.groups()
        if len(tmp) == 4 and tmp[3] == '':
            if len(tmp[2]) <= 3 and len(tmp[2]) > 0:
                print name, email
    return 

for i in range(input()):
    name , email = str(raw_input()).split()
    valid(name, email)