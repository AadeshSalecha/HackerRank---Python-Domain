#Classes: Dealing with Complex Numbers
#by harsh_beria93
#Problem
#Submissions
#Leaderboard
#Discussions
#Editorial
#For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
#
#The real and imaginary precision part should be correct up to two decimal places.
#
#Input Format
#
#One line of input: The real and imaginary part of a number separated by a space.
#
#Output Format
#
#For two complex numbers  and , the output should be in the following sequence on separate lines:
#
# 
#For complex numbers with non-zero real and complex part, the output should be in the following format: 
#
#Replace the plus symbol  with a minus symbol  when .
#
#For complex numbers with a zero complex part i.e. real numbers, the output should be: 
#
#For complex numbers where the real part is zero and the complex part is non-zero, the output should be:
#
#Sample Input
#
#2 1
#5 6
#Sample Output
#
#7.00+7.00i
#-3.00-5.00i
#4.00+17.00i
#0.26-0.11i
#2.24+0.00i
#7.81+0.00i
#Concept
#
#Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here. 
#
#Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality. 
#
#__add__-> Can be overloaded for + operation
#
#__sub__ -> Can be overloaded for - operation
#
#__mul__ -> Can be overloaded for * operation
class complex_number:
    def __init__(self, complex_num):
        self.cn = complex_num
        
    def print_num(self):
        if self.cn.imag > 0.00:
            print str(format(self.cn.real, '.2f')) + '+' + str(format(self.cn.imag, '.2f')) + 'i'
        elif self.cn.imag < 0.00:               
            print str(format(self.cn.real, '.2f')) + str(format(self.cn.imag, '.2f')) + 'i'
        elif self.cn.imag == float(0.00):
            print str(format(self.cn.real, '.2f')) + '+' + str(format(0.00,'.2f')) + 'i'
            
def add(c1, c2):
     complex_number(c1+c2).print_num()
        
def sub(c1, c2):
     complex_number(c1-c2).print_num()
        
def mul(c1, c2):
     complex_number(c1*c2).print_num()
                
def div(c1, c2):
     complex_number(c1/c2).print_num()        
        
def mod(c):
     complex_number(abs(c)).print_num()                
    
c_a, c_c = map(float, str(raw_input()).split())            
c = (complex(c_a, c_c))
d_a, d_c = map(float, str(raw_input()).split())
d = (complex(d_a, d_c))

add(c,d)
sub(c,d)
mul(c,d)
div(c,d)
mod(c)
mod(d)


