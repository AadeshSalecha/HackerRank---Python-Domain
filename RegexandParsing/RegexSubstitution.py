'''
Title     : Regex Substitution
Subdomain : Regex and Parsing
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
import re, sys
n = int(input())
for line in sys.stdin:
    remove_and = re.sub(r'(?<= )(&&)(?= )',"and",line)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )',"or",remove_and)
    print(remove_or,end='')

