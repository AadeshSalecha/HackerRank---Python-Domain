#Find the Second Largest Number
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#You are given  numbers. Store them in a list and find the second largest number.
#
#Input Format 
#The first line contains . The second line contains an array [] of  integers each separated by a space.
#
#Constraints 
# 
#
#Output Format 
#Output the value of the second largest number.
#
#Sample Input
#
#5
#2 3 6 6 5
#Sample Output
#
#5

def largest_num(num):
    largest = -101
    for i in num:
        if i > largest:
            largest = i
        
    return largest

def count_largest(num):
    largest = largest_num(num)
    count = 0
    for i in num:
        if i == largest:
            count += 1
            
    for i in range(count):
        num.remove(largest)
        
    return num
  
n = input()
a = str(raw_input())
a = a.split()

num = []

for i in range(n):
    num.append(int(a[i]))
    
num = count_largest(num)
print largest_num(num)