# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:37:38 2017

@author: dzhao
"""



def fib(x):
    if x == 2:
        return 2
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

sum = 0
result = 0
x = 1
list = []
while result < 4000000:
    if fib(x)%2 == 0:
        sum = sum + fib(x)
    x = x + 1
    result = fib(x)
    list.append(fib(x))
    
print (list)
print (fib(x))
print (sum)