'''
Title     : Set .union() Operation
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
a = input()
s1 = set(map(int,str(raw_input()).split()))

b = input()
s2 = set(map(int,str(raw_input()).split()))

print len(s1.union(s2))