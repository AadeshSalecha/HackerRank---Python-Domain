#Nested Lists
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Tutorial
#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
#Input Format
#
#The first line contains an integer, , the number of students. 
#The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
#Constraints
#
#There will always be one or more students having the second lowest grade.
#Output Format
#
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
#
#Sample Input
#
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39
#Sample Output
#
#Berry
#Harry
#Explanation
#
#There are  students in this class whose names and grades are assembled to build the following list:
#
#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

def second_lowest(num):
    lowest = 1000
    for i in num:
        if i < lowest:
            lowest = i
        
    count = 0
    for i in num:
        if i == lowest:
            count += 1
            
    for i in range(count):
        num.remove(lowest)
        
    second_lowest = 1000
    for i in num:
        if i < second_lowest:
            second_lowest = i
            
    return second_lowest
  
def count_second_lowest(grades,names,second_lowest):
    index = []
    for i in range(len(grades)):
        if grades[i] == second_lowest:
            index.append(i)
            
    result = []
    for i in index:
        result.append(names[i])
        
    return result 
                
n = input()

names = []
grades = []

for i in range(n):
    names.append(str(raw_input()))
    grades.append(float(raw_input()))

second_lowest_grade = second_lowest(grades[:])
result = count_second_lowest(grades, names, second_lowest_grade)
result.sort()
for i in result:
    print i
