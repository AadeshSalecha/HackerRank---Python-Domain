'''
Title     : Validating Roman Numerals
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re
s = str(raw_input())
cpy = s[:]
s = re.search(r'[M]{0,3}(CM|C)?[D]{0,1}[X]{0,1}[C]{0,4}[X]{0,1}[L]{0,1}[I]{0,1}[X]{0,3}[I]{0,1}[V]{0,1}[I]{0,3}', s)

print s.group() == cpy