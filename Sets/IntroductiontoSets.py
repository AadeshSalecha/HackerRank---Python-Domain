'''
Title     : Introduction to Sets
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n = input()

a = str(raw_input())
a = a.split()
s = []
for i in a:
    s.append(int(i))
    
print float(sum(set(s)))/len(set(s))