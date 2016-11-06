'''
Title     : Find Angle MBC
Subdomain : Math
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import math

a = float(input())
b = float(input())

rad = math.atan(a/b)

print str(int(round((rad * 180) / math.pi))) + '°'