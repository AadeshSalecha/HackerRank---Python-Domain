'''
Title     : Check Strict Superset
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
seta = set(map(int, str(raw_input()).split()))

n = input()

other_sets = []
for i in range(n):
    other_sets.append(set(map(int, str(raw_input()).split())))

result = True

for i in other_sets:
    if not(i.issubset(seta)):
        result = False

print result