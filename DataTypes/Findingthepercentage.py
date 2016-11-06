#Finding the percentage
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#Tutorial
#You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#
#Input Format
#
#The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
#
#Constraints
#
#Output Format
#
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
#Sample Input
#
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output
#
#56.00
#Explanation
#
#Marks for Malika are  whose average is 
n = input()

raw_data = []
for i in range(n):
    raw_data.append(str(raw_input()))
    
processed = {}
for i in range(n):
    a = raw_data[i].split()
    processed[a[0]] = [float(a[1]),float(a[2]),float(a[3])]
    
name = str(raw_input())

result = sum(processed[name])/3.00
print ("%.2f" % result)
