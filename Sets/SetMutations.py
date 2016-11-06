'''
Title     : Set Mutations
Subdomain : Sets
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n = input()
seta = set(map(int,str(raw_input()).split()))
other_sets_num = input()

commands = []
other_sets = []
for i in range(other_sets_num):
    commands.append(str(raw_input()))
    other_sets.append(set(map(int, str(raw_input()).split())))
    
for i in range(other_sets_num):
    if (commands[i].split()[0]) == 'intersection_update':
        seta.intersection_update(other_sets[i])
    elif (commands[i].split()[0]) == 'symmetric_difference_update':
        seta.symmetric_difference_update (other_sets[i])
    elif (commands[i].split()[0]) == 'difference_update':
        seta.difference_update  (other_sets[i])
    elif  (commands[i].split()[0]) == 'update':
        seta.update(other_sets[i])
           
print sum(seta)