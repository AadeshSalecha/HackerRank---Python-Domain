'''
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
s = str(raw_input())

a = str(raw_input())
a = a.split()

print s[:int(a[0])] + a[1] + s[int(a[0])+1:] 