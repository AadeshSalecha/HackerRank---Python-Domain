'''
Title     : The Minion Game
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
s = str(raw_input())
length = len(s)
stuart = 0
kevin = 0
for i in xrange(length):
    if s[i].isalpha():
        if s[i] in 'AEIOU':
            kevin += len(s)-i
        else:
            stuart += len(s)-i

if stuart > kevin:
    print 'Stuart ' + str(stuart)
elif kevin > stuart:
    print 'Kevin ' + str(kevin)
else:
    print 'Draw'