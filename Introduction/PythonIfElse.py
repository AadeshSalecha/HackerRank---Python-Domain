'''
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n = input()

if (n % 2 == 0):
    if n == 2 or n== 4:
        print 'Not Weird'
    elif (n >= 6) and (n <= 20):
        print 'Weird'
    else:
        print 'Not Weird'
else:
    print 'Weird'