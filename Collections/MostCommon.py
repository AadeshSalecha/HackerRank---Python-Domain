#Most Common
#by DOSHI
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#You are given a string . 
#The string contains only lowercase English alphabet characters.
#
#Your task is to find the top three most common characters in the string .
#
#Input Format
#
#A single line of input containing the string .
#
#Constraints
#
#
#Output Format
#
#Print the three most common characters along with their occurrence count each on a separate line.
#Sort output in descending order of occurrence count.
#If the occurrence count is the same, sort the characters in ascending order.
#
#Sample Input
#
#aabbbccde
#Sample Output
#
#b 3
#a 2
#c 2
#Explanation
#
#Here, b occurs  times. It is printed first.
#Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c.
#
#Note: The string  has at least  distinct characters.

from collections import *
s = str(raw_input())
s_c = Counter(s)

for j in range(3):
    highest = max(s_c.values())
    if (highest == 1):
        print 'a 1'
        print 'b 1'
        print 'c 1'
        break
    for i in s_c.keys():
        if s_c[i] == highest:
            print i, highest
            del s_c[i]
            break            