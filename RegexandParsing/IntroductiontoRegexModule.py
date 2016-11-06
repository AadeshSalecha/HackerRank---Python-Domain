'''
Title     : Introduction to Regex Module
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
for i in range(int(raw_input())):
    print bool(re.search(r"^(+|-)?\d*\.\d+$",raw_input().strip()))
