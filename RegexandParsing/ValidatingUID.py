'''
Title     : Validating UID
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
from collections import Counter
def valid(uid):
    upper = 0
    digits = 0
    for i in uid:
        if i.isupper():
            upper += 1
        if i.isdigit():
            digits += 1
    if uid.isalnum() and len(uid) == 10 and max((Counter(uid)).values()) == 1 and digits >= 3 and upper >= 2:
        print "Valid"
        return
    print "Invalid"
    return

[valid(str(raw_input())) for i in range(input())]