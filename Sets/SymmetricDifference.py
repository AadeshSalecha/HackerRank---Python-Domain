'''
Title     : Symmetric Difference
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
a = input()
s1 = set(str(raw_input()).split())

b = input()
s2 = set(str(raw_input()).split())


symetric = list((s1.difference(s2)).union((s2.difference(s1))))
symetric = map(int,symetric)
symetric.sort()

for i in symetric: 
    print i