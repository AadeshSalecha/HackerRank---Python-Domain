'''
Title     : Find a string
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
s = str(raw_input())
sub = str(raw_input())

count = 0

while (s.find(sub) != -1):
    count += 1
    s = s[s.find(sub)+len(sub)-1:]
    
print count