'''
Title     : XML 1 - Find the Score
Subdomain : XML
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import collections

n = input()
a = ''
for i in range(n):
    a += str(raw_input())
    
mp = collections.Counter(a)
print int(mp['\'']) / 2