#Zeros and Ones
#by DOSHI
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#zeros
#
#The zeros tool returns a new array with a given shape and type filled with 's.
#
#import numpy
#
#print numpy.zeros((1,2))                    #Default type is float
##Output : [[ 0.  0.]] 
#
#print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
##Output : [[0 0]]
#ones
#
#The ones tool returns a new array with a given shape and type filled with 's.
#
#import numpy
#
#print numpy.ones((1,2))                    #Default type is float
##Output : [[ 1.  1.]] 
#
#print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
##Output : [[1 1]]   
#Task
#
#Your task is to print an array of size  and integer type using the tools zeros and ones.  is the space separated list of the dimensions of the array.
#
#Input Format
#
#A single line containing the space separated list of .
#
#Output Format
#
#First, print the array using the zeros tool and then print the array with the ones tool.
#
#Sample Input
#
#3 3 3
#Sample Output
#
#[[[0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]
#
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]]
#[[[1 1 1]
#  [1 1 1]
#  [1 1 1]]
#
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
#
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]] 

import numpy

args = map(int, str(raw_input()).split())

b = numpy.ones(tuple(args), dtype = int)
a = numpy.zeros(tuple(args), dtype = int)

print a
print b
