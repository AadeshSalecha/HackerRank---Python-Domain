'''
Title     : Re.findall() &amp; Re.finditer()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = str(raw_input())
s = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',s)

if s:
    s = map(lambda x:x[:-1], s)
    print '\n'.join(s)
else:
    print -1