'''
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import textwrap
s = input()
w = int(input().strip())
print(textwrap.fill(s,w))
