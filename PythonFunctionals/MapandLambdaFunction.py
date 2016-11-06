'''
Title     : Map and Lambda Function
Subdomain : Python Functionals
Domain    : Python
Author    : Aadesh Salecha
Created   : August 2016
'''
def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
        
memo = {1:0, 2:1, 3:1, 4:2}    
print map(lambda x: x**3, map(fib, range(1,input()+1)))