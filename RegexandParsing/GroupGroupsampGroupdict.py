'''
Title     : Group(), Groups() &amp; Groupdict()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = re.search(r'([a-zA-Z0-9])(\1)', str(raw_input()))
if (s):
    print s.group(1)
else:
    print -1
