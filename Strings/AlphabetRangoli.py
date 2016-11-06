'''
Title     : Alphabet Rangoli
Subdomain : Strings
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
n = input()

rows = (n*2-1)
line_length = (((n*2-1) * 2)-1)
result = []
for i in range(1,rows/2+1):
    a = '-' * ((line_length - (((i*2-1) * 2) -1))/2)

    for j in range(((((i*2-1) * 2) -1)/2)+1):
        if j % 2 == 0:
            a += str(chr(ord('a') + (n-1) - (j) + (j/2)))
        else:
            a += '-'
    
    b = ''
    for j in range(((((i*2-1) * 2) -1)/2)+1):
        if j % 2 == 0:
            b += '-'
        else:
            b += str(chr(ord('a') + (n-1) - (j/2)))        
    a += b[::-1]
    a += '-' * (((line_length - (((i*2-1) * 2) -1))/2)-1)
    result.append(a)

mid_line = ''
for i in range(line_length/2):
    if i % 2 == 0:
        mid_line += str(chr(ord('a')+(n-1) -i + (i/2)))
    else:
        mid_line += '-'
mid_line += 'a'        
for i in range(line_length/2):
    if i % 2 == 0:
        mid_line += str(chr(ord('a')+(n-1) -(i/2)))
    else:
        mid_line += '-'
tmp = result[::-1]        
result.append(mid_line[:((line_length+1)/2)] + (mid_line[((line_length+1)/2):])[::-1]) 
result += tmp
for i in result:
    print i