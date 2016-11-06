'''
Title     : Hex Color Code
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
a = ''.join((''.join([str(raw_input()) for i in range(input())])).split())
hexs = re.findall(r'#[A-Fa-f0-9]{3,6}', a)

for i in hexs:
    if a[a.index(i)+len(i)] != '{':
        print i
