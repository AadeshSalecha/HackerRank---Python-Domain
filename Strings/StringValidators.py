'''
Title     : String Validators
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
s = str(raw_input())

b = False
for i in s:
    if (i.isalnum()):
        b = True
print b
    

b = False
for i in s:
    if i.isalpha():
        b = True
print b
    

b = False
for i in s:
    if i.isdigit():
        b = True
print b
    
b = False
for i in s:
    if i.islower():
        b = True
print b

b = False
for i in s:
    if i.isupper():
        b = True
print b