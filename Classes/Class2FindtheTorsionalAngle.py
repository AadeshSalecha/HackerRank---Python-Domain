#Class 2 - Find the Torsional Angle
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#You are given four points  and  in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points  and  in degrees(not radians). Let the angle be . 
#
# where  x  and  x .
#
#Here,  means the dot product of  and , and  x  means the cross product of vectors  and . Also, .
#
#Input Format
#
#One line of input containing the space separated floating number values of the  and coordinates of a point.
#
#Output Format
#
#Output the angle correct up to two decimal places.
#
#Sample Input
#
#0 4 5
#1 7 6
#0 5 9
#1 7 2
#Sample Output
#
#8.19
import math

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, other):
        return vector(self.x-other.x, self.y-other.y, self.z-other.z)
    def __add__(self, other):
        return vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def dot(self, other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    def cross(self, other):
        return vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
    def mod(self):
        return pow((self.x**2+ self.y**2 + self.z**2),0.5)
    
a = vector(*map(float, raw_input().strip().split()))
b = vector(*map(float, raw_input().strip().split()))
c = vector(*map(float, raw_input().strip().split()))
d = vector(*map(float, raw_input().strip().split()))

ab = b - a
bc = c - b
cd = d - c
x = ab.cross(bc)
y = bc.cross(cd)
print round(math.degrees(math.acos(((x.dot(y))/(x.mod()* y.mod())))),2)
