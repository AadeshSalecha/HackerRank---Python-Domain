'''
Title     : Matrix Script
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
def f(s):
    result = re.sub(r'[!@#$%&\s]',' ', s.group())
    return result

n, m = map(int, str(raw_input()).split())

a = []
message = ''
for i in range(n):
    a.append(str(raw_input()))
    
for i in range(m):
    for j in range(n):
        message += a[j][i]
        
message = re.sub(r'[a-zA-Z0-9][!@#$%&\s]+[a-zA-Z0-9]',f, message)  
print message
