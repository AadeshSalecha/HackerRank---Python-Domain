'''
Title     : Merge the Tools!
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
def compress(s):
    result = ''
    for i in s:
        if i not in result:
            result += i
    return (result)

import textwrap
s = str(raw_input())
k = input()

a = textwrap.fill(s, k).split('\n')
for i in a:
    print compress(i)