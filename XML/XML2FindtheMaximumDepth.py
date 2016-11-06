'''
Title     : XML2 - Find the Maximum Depth
Subdomain : XML
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
a  = ''.join([str(raw_input()) for i in range(input())])
a = a[a.find('<')+1:]
depths = []
cur_depth = 0
for i in range(len(a)):
    if a[i] == '<' and a[i+1] != '/':
        cur_depth += 1
        depths.append(cur_depth)
    if (a[i] == '<' and a[i+1] == '/') or (a[i] == '/' and a[i+1] == '>'):
        cur_depth -= 1
        depths.append(cur_depth)

print max(max(depths),0)

