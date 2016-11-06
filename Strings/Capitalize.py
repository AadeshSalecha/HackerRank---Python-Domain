'''
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
s = str(raw_input())
result = ''
a = True

for i in range(len(s)):
    if a:
        result += s[i].upper()
        a = False
    else:
        result += s[i].lower()
    if s[i] == ' ':
        a = True

print result