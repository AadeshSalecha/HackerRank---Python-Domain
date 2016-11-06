'''
Title     : Polar Coordinates
Subdomain : Math
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import cmath
num = input()     
print pow(num.real**2 + num.imag**2, 0.5)    
print cmath.phase(num)            