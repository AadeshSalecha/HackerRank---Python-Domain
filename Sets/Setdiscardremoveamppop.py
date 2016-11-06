'''
Title     : Set .discard(), .remove() &amp; .pop()
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
input()
s = set(map(int,str(raw_input()).split()))
n = input()
commands = []
for i in range(n):
    commands.append(str(raw_input()))

for i in commands:
    a = i.split()
    if (a[0] == 'pop'):
        s.pop()
    if(a[0] == 'remove'):
        s.remove(int(a[1]))
    if(a[0] == 'discard'):
        s.discard(int(a[1]))

print sum(s)