#Lists
#by shashank21j
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Tutorial
#Task 
#Initialize your list (L = []) and follow the  commands given over  lines.
#
#Each command will be  of the  commands given above. The extend() method will not be used. Each command will have its own value(s) separated by a space.
#
#Input Format
#
#The first line contains an integer,  (the number of commands). 
#The  subsequent lines each contain one of the  commands described above.
#
#Sample Input
#
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print 
#remove 6
#append 9
#append 1
#sort 
#print
#pop
#reverse
#print
#Sample Output
#
#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]

def do(s, L):
    if (s.split()[0] == 'insert'):
        L.insert(int(s.split()[1]),int(s.split()[2]))
    elif (s.split()[0] == 'remove'):    
        L.remove(int(s.split()[1]))
    elif (s.split()[0] == 'append'):
        L.append(int(s.split()[1]))
    elif (s.split()[0] == 'reverse'):
        L.reverse()
    elif (s.split()[0] == 'pop'):
        L.pop()
    elif (s.split()[0] == 'sort'):
        L = L.sort()
    elif (s.split()[0] == 'print'):
        print L
        L = []
    return 

n = input()

L = []
s = []

for i in range(n):
    s.append(str(raw_input()))

for i in range(n):
    do(s[i],L)


    
