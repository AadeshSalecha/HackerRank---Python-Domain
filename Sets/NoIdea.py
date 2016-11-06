'''
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n,m = map(int,str(raw_input()).split())
a = str(raw_input()).split()

s1 = set(str(raw_input()).split())
s2 = set(str(raw_input()).split())

happiness = 0
for i in a:
    if i in s1:
        happiness += 1
    if i in s2:
        happiness -= 1
        
print happiness