'''
Title     : Map and Lambda Function
Subdomain : Python Functionals
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
def valid(email):
    at_index = email.find('@')
    if at_index == 0:
        return False
    
    for i in email[:at_index]:
        if i.isalnum() == False and i != '_' and i != '-':
            return False
        
    dot_index = email.find('.')
    for i in email[at_index+1:dot_index]:
        if i.isalnum() == False:
            return False
        
    if (dot_index == at_index or dot_index < at_index):
        return False
    if len(email[dot_index+1:]) > 3:
        return False
    return True
    
    
n = input()
emails = []

for i in range(n):
    emails.append(str(raw_input()))

    
result = []
for i in emails:
    if valid(i):
        result.append(i)
        
result.sort()
print result