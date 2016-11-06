'''
Title     : Re.start() &amp; Re.end()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = str(raw_input())
k = str(raw_input())

matches = re.finditer(r'(?='+k+')', s)
a = False
for results in matches:
    print tuple([results.start(), results.start() + len(k)-1])
    a = True
      
if not a:
    print (-1, -1)