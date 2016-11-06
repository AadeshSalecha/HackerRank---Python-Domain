'''
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n = input()

d = set([])
for i in range(n):
    d.add(str(raw_input()))
    
print len(d)