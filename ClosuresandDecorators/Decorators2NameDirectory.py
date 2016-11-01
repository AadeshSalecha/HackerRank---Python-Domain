#Decorators 2 - Name Directory
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Let's use decorators to build a name directory! You are given some information about people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.
#
#For Henry Davids, the output should be:
#
#Mr. Henry Davids
#For Mary George, the output should be:
#
#Ms. Mary George
#Input Format
#
#The first line contains the integer , the number of people.
# lines follow each containing the space separated values of the first name, last name, age and sex, respectively.
#
#Constraints
#
#
#Output Format
#
#Output  names on separate lines in the format described above in ascending order of age.
#
#Sample Input
#
#3
#Mike Thomson 20 M
#Robert Bustle 32 M
#Andria Bustle 30 F
#Sample Output
#
#Mr. Mike Thomson
#Ms. Andria Bustle
#Mr. Robert Bustle
#Concept
#
#For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it here. 

from operator import *

n = input()

lib = []
for i in range(n):
    a = str(raw_input()).split()
    if a[3] == 'M':
        lib.append(list([str('Mr. '+a[0]+ ' '+a[1]), int(a[2])]))
    else:
        lib.append(list([str('Ms. '+a[0]+ ' '+a[1]), int(a[2])]))

lib.sort(key=itemgetter(1))
for i in lib:
    print i[0]