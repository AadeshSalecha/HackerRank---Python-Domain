'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    
    return leap
