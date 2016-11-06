#Maximize It!
#by anuj_95
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#You are given a function .
#
#You are also given  lists. The  list consists of  elements.
#
#You have to pick exactly one element from each list so that the equation below is maximized: 
#
#%
#
# denotes the element picked from the  list . Find the maximized value  obtained.
#
# denotes the modulo operator.
#
#Input Format 
#The first line contains  space separated integers  and . 
#The next  lines each contains an integer  followed by  space separated integers denoting the elements in the list.
#
#Output Format 
#Output a single integer denoting the value .
#
#Constraints 
# 
# 
# 
#
#Sample Input
#
#3 1000
#2 5 4
#3 7 8 9 
#5 5 7 8 9 10 
#Sample Output
#
#206
#Explanation
#
#Picking  from the st list,  from the nd list and  from the rd list gives the maximum value equal to % = .

import itertools
k , m = map(int, str(raw_input()).split())
print max([sum(i)%m for i in list(itertools.product(*[([x**2 for x in (map(int, str(raw_input()).split())[1:])]) for i in range(k)]))])