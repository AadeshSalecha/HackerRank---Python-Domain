#Tuples
#by shashank21j
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Tutorial
#Task 
#Given an integer, , and  space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of .
#
#Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
#
#Input Format
#
#The first line contains an integer, , denoting the number of elements in the tuple. 
#The second line contains  space-separated integers describing the elements in tuple .
#
#Output Format
#
#Print the result of .
#
#Sample Input
#
#2
#1 2
#Sample Output
#
#3713081631934410656

n = input()

s = str(raw_input())
s1 = s.split()

if len(s1) != n:
    raise Exception
    
t = []
for i in range(n):
    t.append(int(s1[i]))
    
t = tuple(t)
print hash(t)
